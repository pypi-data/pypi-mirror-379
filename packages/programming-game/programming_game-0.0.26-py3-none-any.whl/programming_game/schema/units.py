from typing import Literal

import msgspec

from . import intents
from .items import Helm, Weapon, Shield
from .other import InventoryType, PlayerStats, UnitTrades
from .position import Position
from .quest import ActiveQuest, AvailableQuest
from ..utils import get_distance


class UnitBase(msgspec.Struct, tag=True, kw_only=True, repr_omit_defaults=True):
    unitsInSight: dict[str, "AnyUnit"]
    calories: float
    id: str
    name: str
    hp: float
    tp: float
    mp: float
    position: Position
    lastUpdate: int
    intent: intents.AnyIntent | None  # noqa
    inventory: InventoryType
    npc: bool
    race: str
    trades: UnitTrades
    action: Literal["cast", "craft", "equipSpell", "harvest"] | None = None
    actionDuration: float | None = None
    actionStart: float | None = None
    actionTarget: str | None = None
    actionUsing: str | None = None

    extraData: dict = msgspec.field(default_factory=dict)


class NPC(UnitBase, tag="npc", kw_only=True):
    banker: bool
    availableQuests: dict[str, AvailableQuest] = {}


class Monster(UnitBase, tag="monster", kw_only=True):
    monsterId: str
    spawned: int
    threat: dict[str, float]
    focus: str | None


class PlayerEquipment(msgspec.Struct, ):
    helm: str | None
    weapon: str | None
    offhand: str | None

    @property
    def items(self) -> list[str]:
        return [getattr(self, f) for f in self.__struct_fields__ if getattr(self, f)]


class Player(UnitBase, tag="player", kw_only=True):
    bounty: float
    role: str
    stats: PlayerStats
    quests: dict[str, ActiveQuest] = {}
    equipment: PlayerEquipment
    storage: InventoryType

    # completedQuests: Any = [] # only serverside used .. not send to client

    def __repr__(self) -> str:
        return f"<Player name='{self.name}' hp='{self.hp:.2f}' calories='{self.calories:.2f}' position='{self.position}'>"

    @staticmethod
    def attack(target_id: str) -> intents.AttackIntent:
        """Attacks a target unit."""

        return intents.AttackIntent(target=target_id)

    @staticmethod
    def move(position: Position) -> intents.MoveIntent:
        return intents.MoveIntent(position=position)

    def move_to(self, x: float | Position, y: float | None = None) -> intents.MoveIntent | None:
        """Convenience method to move the player to x,y coordinates."""
        if isinstance(x, Position):
            if y is not None:
                raise ValueError("Cannot specify y when passing a Position")
            target = x
        else:
            if y is None:
                raise ValueError("Must specify y when passing x")
            target = Position(x=x, y=y)

        if get_distance(self.position, target) > 0.1:
            return self.move(target)
        return None

    @staticmethod
    def respawn() -> intents.RespawnIntent:
        """Sends the respawn intent to the server."""
        return intents.RespawnIntent()

    @staticmethod
    def summon_mana() -> intents.BaseIntent:
        """Summons mana."""
        return intents.BaseIntent()

    def eat(self, food_id: str) -> intents.EatIntent:
        """Eats a food item."""
        return intents.EatIntent(item=food_id, save=int(self.inventory.get(food_id, 0) - 1))

    @staticmethod
    def equip_spell(spell_name: str) -> intents.EquipSpellIntent:
        """Equips a spell."""
        return intents.EquipSpellIntent(spell=spell_name)

    @staticmethod
    def unequip_spell() -> intents.UnequipSpellIntent:
        """Unequips a spell."""
        return intents.UnequipSpellIntent()

    @staticmethod
    def cast(spell_name: str, target_id: str | None = None) -> intents.CastSpellIntent:
        """Casts a spell on an optional target."""
        return intents.CastSpellIntent(spell=spell_name, target=target_id)

    @staticmethod
    def sell(items: dict[str, float], to_npc_id: str) -> intents.SellItemsIntent:
        """Sells items to an NPC."""
        return intents.SellItemsIntent(items=items, to=to_npc_id)

    @staticmethod
    def buy(items: dict[str, int], from_npc_id: str) -> intents.BuyItemsIntent:
        """Buys items from an NPC."""
        return intents.BuyItemsIntent(items=items, from_=from_npc_id)

    @staticmethod
    def use(item_name: str, until: int, target_id: str | None = None) -> intents.UseIntent:
        """Uses an item, optionally on a target."""
        return intents.UseIntent(item=item_name, until=until, target=target_id)

    @staticmethod
    def equip(item_name: str, slot: str) -> intents.EquipIntent:
        """Equips an item in the specified slot."""
        return intents.EquipIntent(item=item_name, slot=slot)

    @staticmethod
    def unequip(slot: str) -> intents.UnEquipIntent:
        """Unequips an item from the specified slot."""
        return intents.UnEquipIntent(slot=slot)

    @staticmethod
    def set_role(role: str) -> intents.SetRoleIntent:
        """Sets the player's role in a party."""
        return intents.SetRoleIntent(role=role)

    @staticmethod
    def invite_to_party(target_id: str) -> intents.InviteToPartyIntent:
        """Invites a target to the party."""
        return intents.InviteToPartyIntent(target=target_id)

    @staticmethod
    def seek_party() -> intents.BaseIntent:
        """Announces that the player is seeking a party."""
        return intents.BaseIntent("seekParty")

    @staticmethod
    def accept_party_invite(inviter_id: str) -> intents.AcceptPartyEventIntent:
        """Accepts a party invite."""
        return intents.AcceptPartyEventIntent(inviter=inviter_id)

    @staticmethod
    def decline_party_invite(inviter_id: str) -> intents.DeclinePartyEventIntent:
        """Declines a party invite."""
        return intents.DeclinePartyEventIntent(inviter=inviter_id)

    @staticmethod
    def leave_party() -> intents.LeavePartyIntent:
        """Leaves the current party."""
        return intents.LeavePartyIntent()

    @staticmethod
    def craft(item_name: str, resources: dict[str, int]) -> intents.CraftIntent:
        """Crafts an item using resources."""
        return intents.CraftIntent(item=item_name, from_=resources)

    @staticmethod
    def use_weapon_skill(skill_name: str, target_id: str) -> intents.WeaponSkillIntent:
        """Uses a weapon skill on a target."""
        return intents.WeaponSkillIntent(skill=skill_name, target=target_id)

    @staticmethod
    def drop(item_id: str, until: int) -> intents.DropIntent:
        """Drops an item."""
        return intents.DropIntent(item=item_id, until=until)

    @staticmethod
    def set_trade(
            buying: dict[str, dict[str, int]], selling: dict[str, dict[str, int]]
    ) -> intents.SetTradeIntent:
        """Sets the player's trade offers."""
        return intents.SetTradeIntent(buying=buying, selling=selling)

    @staticmethod
    def accept_quest(npc_id: str, quest_name: str) -> intents.AcceptQuestIntent:
        """Accepts a quest from an NPC."""
        return intents.AcceptQuestIntent(npcId=npc_id, questId=quest_name)

    @staticmethod
    def abandon_quest(*, quest_name: str) -> intents.AbandonQuestIntent:
        """Abandons a quest."""
        return intents.AbandonQuestIntent(quest=quest_name)

    @staticmethod
    def turn_in_quest(npc_id: str, quest_name: str) -> intents.TurnInQuestIntent:
        """Turns in a quest to an NPC."""
        return intents.TurnInQuestIntent(npcId=npc_id, questId=quest_name)

    @staticmethod
    def deposit(banker_id: str, items: InventoryType) -> intents.DepositIntent:
        """Deposits items into storage."""
        return intents.DepositIntent(npcId=banker_id, until=items)

    @staticmethod
    def withdraw(banker_id: str, items: InventoryType) -> intents.WithdrawIntent:
        """Withdraws items from storage."""
        return intents.WithdrawIntent(npcId=banker_id, until=items)


AnyUnit = NPC | Monster | Player
