import asyncio
import contextlib
import logging
import time
from dataclasses import dataclass, field
from pprint import pprint
from typing import TYPE_CHECKING, Any, Protocol

import msgspec

from programming_game.schema import events
from programming_game.schema.events import BaseEvent
from programming_game.schema.game_object import AnyGameObject
from programming_game.schema.intents import WeaponSkillIntent
from programming_game.schema.items import AnyItem, Item
from programming_game.schema.position import Position
from programming_game.schema.units import AnyUnit, Monster
from programming_game.structure.game_state import GameState, InternalGameState
from programming_game.structure.instance import Instance
from programming_game.structure.on_tick_response import OnTickResponse
from programming_game.utils import to_snake_case

logger = logging.getLogger(__name__)

if TYPE_CHECKING:
    from programming_game.client import GameClient


class ScriptProtocol(Protocol):
    """
    Protocol for bot scripts.

    The script must implement an async on_tick method that returns:
    - AnyIntent: The intent will be sent to the server
    - int/float: Pause the next tick by this many seconds
    - None/bool: No action, continue with normal tick timing
    """

    async def on_tick(self) -> OnTickResponse: ...


def parse_items(event_items):
    try:
        return msgspec.convert(event_items, dict[str, AnyItem])
    except msgspec.ValidationError:
        items = {}
        custom_types = {}

        base_field_names = {f.name for f in msgspec.structs.fields(Item)}
        base_field_names.add("type")

        for item_name, data in event_items.items():
            try:
                new_item = msgspec.convert(data, AnyItem)
                items[item_name] = new_item
            except msgspec.ValidationError:
                new_type_name = data.get("type")
                if new_type_name in custom_types:
                    try:
                        items[item_name] = msgspec.convert(data, custom_types[new_type_name])
                        logger.warning(f"Using custom type {new_type_name} for item {item_name}")
                    except msgspec.ValidationError:
                        logger.error(f"Invalid data for custom type {new_type_name}: {data}")
                    finally:
                        continue
                try:
                    fields = []
                    for name, value in data.items():
                        if name not in base_field_names:
                            field_type = type(value)
                            if field_type is dict:
                                field_type = Any
                            fields.append((name, field_type))
                    class_name = new_type_name.capitalize()
                    NewType = msgspec.defstruct(
                        name=class_name, fields=fields, bases=(Item,), tag=new_type_name
                    )
                    custom_types[new_type_name] = NewType
                    new_item = msgspec.convert(data, NewType)
                    items[new_item.id] = new_item
                    logger.warning(f"Created Item type {class_name} from unknown item: {item_name}")
                except Exception as e:
                    logger.error(f"Error creating item type: {e} {item_name} {data}")
        return items


class EventMixinProtocol(Protocol):
    game_state: "GameState"
    instance: "Instance"


class EventMixin:
    def handle_unit_disappeared_event(self: EventMixinProtocol, event: events.UnitDisappearedEvent) -> None:
        self.game_state.units.pop(event.unitId, None)

    def handle_unit_appeared_event(self: EventMixinProtocol, event: events.UnitAppearedEvent) -> None:
        self.game_state.units[event.unit.id] = event.unit
        # TODO: unique Items  # keys(event.uniqueItems).forEach((uniqueItemId) = > {  #    char.uniqueItems[uniqueItemId] = event.uniqueItems[uniqueItemId];  # });

    def handle_despawn_event(self: EventMixinProtocol, event: events.DespawnEvent) -> None:
        self.game_state.units.pop(event.unitId, None)

    def handle_moved_event(self: EventMixinProtocol, event: events.MovedEvent) -> None:
        if unit := self.game_state.units.get(event.id):
            unit.position = Position(x=event.x, y=event.y)
        # else:
        #    logger.debug(f"Moved event error: {event.id} not found in units")

    def handle_calories_event(self: EventMixinProtocol, event: events.CaloriesEvent) -> None:
        if unit := self.game_state.units.get(event.unitId):
            unit.calories = event.calories
        else:
            logger.debug(f"Calories event error: {event.unitId} not found in units")

    def handle_set_intent_event(self: EventMixinProtocol, event: events.SetIntentEvent) -> None:
        if unit := self.game_state.units.get(event.unitId):
            unit.intent = event.intent  # TODO: clearUnitActions
        else:
            logger.debug(f"SetIntent event error: {event.unitId} not found in units")

    def handle_spell_event(self: EventMixinProtocol, event: events.CastSpellEvent):
        if unit := self.game_state.units.get(event.unitId):
            unit.action = None
            unit.actionStart = None
            unit.actionDuration = None
            unit.actionTarget = None

    def handle_began_casting_event(self: EventMixinProtocol, event: events.BeganCastingEvent) -> None:
        if unit := self.game_state.units.get(event.unitId):
            unit.action = "cast"
            unit.actionStart = time.time()
            unit.actionDuration = event.duration
            unit.actionTarget = event.target
        pass

    def handle_tp_event(self: EventMixinProtocol, event: events.TpEvent):
        if unit := self.game_state.units.get(event.unitId):
            unit.tp = event.tp
        else:
            logger.debug(f"Tp event error: {event.unitId} not found in units")

    def handle_hp_event(self: EventMixinProtocol, event: events.HpEvent) -> None:
        if unit := self.game_state.units.get(event.unitId):
            unit.hp = event.hp
        else:
            logger.debug(f"Hp event error: {event.unitId} not found in units")

    def handle_mp_event(self: EventMixinProtocol, event: events.MpEvent) -> None:
        if unit := self.game_state.units.get(event.unitId):
            unit.mp = event.mp
        else:
            logger.debug(f"Mp event error: {event.unitId} not found in units")

    def handle_used_weapon_skill_event(self: EventMixinProtocol, event: events.UsedWeaponSkillEvent):
        if unit := self.game_state.units.get(event.unitId):
            unit.tp = event.tp
            if unit == self.game_state.player and isinstance(unit.intent, WeaponSkillIntent) and unit.intent.skill == event.skill:
                logging.warning("cleared intent from player after weapon skill")
                unit.intent = None

    def handle_attacked_event(self: EventMixinProtocol, event: events.AttackedEvent) -> None:
        if attacker := self.game_state.units.get(event.attacker):
            attacker.tp = event.attackerTp
        else:
            logger.debug(f"Attacked event error: {event.attacker} not found in units")

        if attacked := self.game_state.units.get(event.attacked):
            attacked.hp = event.hp
        else:
            logger.debug(f"Attacked event error: {event.attacked} not found in units")

    def handle_died_event(self: EventMixinProtocol, event: events.DiedEvent) -> None:
        if unit := self.game_state.units.get(event.unitId):
            unit.hp = 0

    def handle_loot_event(self: EventMixinProtocol, event: events.LootEvent) -> None:
        if unit := self.game_state.units.get(event.unitId):
            for item_id, amount in event.items.items():
                unit.inventory[item_id] = unit.inventory.get(item_id, 0) + amount
        else:
            logger.debug(f"Loot event error: {event.unitId} not found in units")

    def handle_inventory_event(self: EventMixinProtocol, event: events.InventoryEvent) -> None:
        if unit := self.game_state.units.get(event.unitId):
            for item_id, amount in event.inventory.items():
                if amount <= 0:
                    unit.inventory.pop(item_id, None)
                else:
                    unit.inventory[item_id] = amount
        else:
            logger.debug(f"Inventory event error: {event.unitId} not found in units")

    def handle_object_appeared_event(self: EventMixinProtocol, event: events.ObjectAppearedEvent) -> None:
        self.gameObjects[event.object.id] = event.object

    def handle_object_disappeared_event(self: EventMixinProtocol, event: events.ObjectDisappearedEvent) -> None:
        try:
            del self.gameObjects[event.objectId]
        except KeyError:
            logger.debug(
                f"{self.instance.instance_id} ObjectDisappeared event error: {event.objectId} not found in gameObjects"
            )

    def handle_ate_event(self: EventMixinProtocol, event: events.AteEvent) -> None:
        if unit := self.game_state.units.get(event.unitId):
            logger.info(
                f"Ate event: {event.item} from {event.unitId} {hasattr(unit, 'calories')} {hasattr(unit, 'inventory')}  {event.calories} {event.remaining}"
            )
            if hasattr(unit, "calories"):
                unit.calories = event.calories
            if hasattr(unit, "inventory"):
                if event.remaining <= 0:
                    with contextlib.suppress(KeyError):
                        del unit.inventory[event.item]
                else:
                    unit.inventory[event.item] = event.remaining
        else:
            logger.debug(f"Ate event error: {event.unitId} not found in units")

    def handle_accepted_quest_event(self: EventMixinProtocol, event: events.AcceptedQuestEvent) -> None:
        logger.info(f"Quest accepted: {event.quest.name} ({event.quest.id}) for unit: {event.unitId}")
        if player := self.game_state.player:
            player.quests[event.quest.id] = event.quest
        if self.character_id == event.unitId and (npc := self.game_state.units.get(event.quest.start_npc)):
            npc.availableQuests.pop(event.quest.id, None)

    def handle_quest_completed_event(self: EventMixinProtocol, event: events.QuestCompletedEvent) -> None:
        if unit := self.game_state.units.get(event.unitId):
            unit.quests.pop(event.questId, None)
        logger.info(f"Quest completed: {event.questId} for unit: {event.unitId} {unit.quests}")

    def handle_quest_update_event(self: EventMixinProtocol, event: events.QuestUpdateEvent) -> None:
        if unit := self.game_state.player:
            if unit.id == event.unitId:
                unit.quests[event.quest.id] = event.quest

    def handle_focus_event(self: EventMixinProtocol, event: events.FocusEvent) -> None:
        if unit := self.game_state.units.get(event.monsterId):
            if isinstance(unit, Monster):
                unit.focus = event.focus
            else:
                logger.error(f"Focus event error: {unit} {event.monsterId} is not a monster")
        else:
            logger.debug(f"Focus event error: {event.monsterId} not found in units")

    def handle_stats_event(self: EventMixinProtocol, event: events.StatsEvent) -> None:
        if unit := self.game_state.units.get(event.unitId):
            if hasattr(unit, "stats"):
                unit.stats = event.stats

    def handle_deposited_event(self: EventMixinProtocol, event: events.DepositedEvent) -> None:
        """Handle items being deposited into storage (removed from inventory)."""
        if player := self.game_state.player:
            for item_id, amount in event.items.items():
                current_amount = player.inventory.get(item_id, 0)
                player.inventory[item_id] = max(0, current_amount - amount)
                if player.inventory[item_id] <= 0:
                    player.inventory.pop(item_id, None)

                current_storage = player.storage.get(item_id, 0)
                player.storage[item_id] = current_storage + amount

    def handle_withdrew_event(self: EventMixinProtocol, event: events.WithdrewEvent) -> None:
        """Handle items being withdrawn from storage (added to inventory)."""
        if player := self.game_state.player:
            for item_id, amount in event.items.items():
                current_amount = player.inventory.get(item_id, 0)
                player.inventory[item_id] = current_amount + amount

                current_storage = player.storage.get(item_id, 0)
                player.storage[item_id] = current_storage - amount

    def handle_traded_event(self: EventMixinProtocol, event: events.TradedEvent) -> None:
        if gave_unit := self.game_state.units.get(event.actingUnitId):
            for item, count in event.gave.items():
                self.game_state.units[gave_unit.id].inventory[item] = self.game_state.player.inventory.get(item, 0) - count
                if self.game_state.units[gave_unit.id].inventory[item] <= 0:
                    self.game_state.units[gave_unit.id].inventory.pop(item, None)
            for item, count in event.got.items():
                self.game_state.player.inventory[item] = self.game_state.player.inventory.get(item, 0) + count

    async def handle_connection_event(
            self: EventMixinProtocol, event: events.ConnectionEvent, client: "GameClient"
    ) -> None:
        assert self.character_id == event.player.id

        if event.items:
            items = parse_items(event.items)
            await client.set_items_and_constants(items, event.constants)

        self.units = event.units
        self.game_state.units = event.units
        self.game_state.items = client._items
        self.gameObjects = event.gameObjects

        # TODO: uniqueItems
        # TODO: gameObjects

        logger.info(f"Game state initialized for player: {event.player.id} in {self.instance.instance_id}")


@dataclass(kw_only=True)
class InstanceCharacter(EventMixin):
    character_id: str
    game_state: "InternalGameState"
    instance: "Instance"
    _script: ScriptProtocol | None = None
    tick_time: float
    tick_events: list[BaseEvent] = field(default_factory=list)
    next_tick_time: float = 0.0
    units: dict[str, "AnyUnit"] = field(default_factory=dict)
    uniqueItems: dict[str, Any] = field(default_factory=dict)
    gameObjects: dict[str, "AnyGameObject"] = field(default_factory=dict)
    _tick_task: asyncio.Task[Any] | None = None
    last_intent_time: float = 0.0

    # Character-specific runtime data
    _tick_task: asyncio.Task[Any] | None = None
    last_intent_time: float = 0.0

    def handle_storage_emptied_event(self, event: events.StorageEmptiedEvent) -> None:
        """Handle storage being emptied (no inventory changes needed)."""
        logger.info("Player storage has been emptied")

    async def handle_event(self, event: BaseEvent, client: "GameClient") -> None:
        match event:
            case events.MovedEvent():
                self.handle_moved_event(event)
            case events.CaloriesEvent():
                self.handle_calories_event(event)
            case events.SetIntentEvent():
                self.handle_set_intent_event(event)
            case events.ConnectionEvent():
                await self.handle_connection_event(event, client)
            case events.UnitAppearedEvent():
                self.handle_unit_appeared_event(event)
            case events.UnitDisappearedEvent():
                self.handle_unit_disappeared_event(event)
            case events.DespawnEvent():
                self.handle_despawn_event(event)
            case events.MpEvent():
                self.handle_mp_event(event)
            case events.HpEvent():
                self.handle_hp_event(event)
            case events.AttackedEvent():
                self.handle_attacked_event(event)
            case events.ObjectAppearedEvent():
                self.handle_object_appeared_event(event)
            case events.ObjectDisappearedEvent():
                self.handle_object_disappeared_event(event)
            case events.AteEvent():
                self.handle_ate_event(event)
            case events.AcceptedQuestEvent():
                self.handle_accepted_quest_event(event)
            case events.QuestCompletedEvent():
                self.handle_quest_completed_event(event)
            case events.LootEvent():
                self.handle_loot_event(event)
            case events.FocusEvent():
                self.handle_focus_event(event)
            case events.DepositedEvent():
                self.handle_deposited_event(event)
            case events.WithdrewEvent():
                self.handle_withdrew_event(event)
            case events.StorageEmptiedEvent():
                self.handle_storage_emptied_event(event)
            case events.StatsEvent():
                self.handle_stats_event(event)
            case events.InventoryEvent():
                self.handle_inventory_event(event)
            case events.QuestUpdateEvent():
                self.handle_quest_update_event(event)
            case events.CastSpellEvent():
                self.handle_spell_event(event)
            case events.BeganCastingEvent():
                self.handle_began_casting_event(event)
            case events.TpEvent():
                self.handle_tp_event(event)
            case events.TradedEvent():
                self.handle_traded_event(event)
            case events.UsedWeaponSkillEvent:
                self.handle_used_weapon_skill_event(event)
            case _:
                logger.warning(f"old event: {event}")
                event_type = type(event)
                handler_name = "handle_" + to_snake_case(event_type.__name__)

                if cb := getattr(self, handler_name, None):
                    if asyncio.iscoroutinefunction(cb):
                        await cb(event)
                    else:
                        cb(event)
                else:
                    logger.warning(f"missing {handler_name}")
