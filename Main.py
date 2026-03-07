# meta developer: @Honorpadx9lte

from .. import loader, utils
from telethon.tl.types import Message

@loader.tds
class KrestikiPvPMod(loader.Module):
    """Крестики-нолики 3x3: управление текстом (1а, 2б...)"""
    strings = {"name": "KrestikiPvP"}

    async def client_ready(self, client, db):
        self.db = db
        self.client = client

    async def krestcmd(self, message: Message):
        """<@юзернейм> - Играть (координаты: 1а, 2б...)"""
        args = utils.get_args_raw(message)
        if not args:
            return await utils.answer(message, "<b>Укажи @юзернейм противника!</b>")
        
        try:
            user = await self.client.get_entity(args)
            game_data = {
                "board": ["⬜️"] * 9,
                "turn": "❌",
                "p1": message.sender_id, 
                "p2": user.id,
                "p2_name": user.first_name,
                "chat_id": message.chat_id,
                "msg_id": message.id
            }
            self.db.set("KrestikiPvP", "game", game_data)
            await self._display(message, game_data)
        except Exception:
            await utils.answer(message, "<b>Юзер не найден!</b>")

    async def watcher(self, message):
        if not isinstance(message, Message) or not message.text: return
        game = self.db.get("KrestikiPvP", "game")
        if not game or message.chat_id != game["chat_id"]: return

        txt = message.text.lower().strip()
        coords = {"1а":0,"1б":1,"1в":2,"2а":3,"2б":4,"2в":5,"3а":6,"3б":7,"3в":8}

        if txt in coords:
            cur = game["p1"] if game["turn"] == "❌" else game["p2"]
            if message.sender_id != cur: return
            
            idx = coords[txt]
            if game["board"][idx] != "⬜️": return

            game["board"][idx] = game["turn"]
            try: await message.delete()
            except: pass
            
            if self._check(game["board"]):
                await self._display(message, game, win=game["turn"])
                self.db.set("KrestikiPvP", "game", None)
            elif "⬜️" not in game["board"]:
                await self._display(message, game, win="draw")
                self.db.set("KrestikiPvP", "game", None)
            else:
                game["turn"] = "⭕️" if game["turn"] == "❌" else "❌"
                self.db.set("KrestikiPvP", "game", game)
                await self._display(message, game)

    async def _display(self, message, g, win=None):
        b = g["board"]
        res = (f"<b>Крестики-нолики 3x3</b>\n\n"
               f"   <b>А</b> <b>Б</b> <b>В</b>\n"
               f"<b>1</b> {b[0]} {b[1]} {b[2]}\n"
               f"<b>2</b> {b[3]} {b[4]} {b[5]}\n"
               f"<b>3</b> {b[6]} {b[7]} {b[8]}\n\n")
        
        if win:
            res += f"<b>🏆 {'Ничья' if win=='draw' else 'Победил ' + win}</b>"
        else:
            opp = f"<a href='tg://user?id={g['p2']}'>{g['p2_name']}</a>"
            name = "Твой" if g["turn"] == "❌" else opp
            res += f"<b>Ход: {g['turn']} ({name})</b>\n<i>Пиши: 1а, 2б...</i>"

        await self.client.edit_message(g["chat_id"], g["msg_id"], res)

    def _check(self, b):
        v = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
        for r in v:
            if b[r[0]] == b[r[1]] == b[r[2]] != "⬜️":
                return True
        return False
