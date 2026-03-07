# meta developer: @Honorpadx9lte

from .. import loader, utils
from telethon.tl.types import Message
import asyncio

@loader.tds
class KrestikiPvPMod(loader.Module):
    """Крестики-нолики PvP по координатам (1а, 2б...)"""
    strings = {"name": "KrestikiPvP"}

    async def client_ready(self, client, db):
        self.db = db
        self.client = client

    async def krestcmd(self, message: Message):
        """<@юзернейм> - Играть с другом (управление: 1а, 2б...)"""
        args = utils.get_args_raw(message)
        if not args:
            return await utils.answer(message, "<b>Укажи @юзернейм противника!</b>")
        
        try:
            user = await self.client.get_entity(args)
            opponent_id = user.id
            opponent_name = user.first_name
        except Exception:
            return await utils.answer(message, "<b>Пользователь не найден!</b>")

        board = ["⬜️"] * 9
        game_data = {
            "board": board,
            "turn": "❌",
            "p1": message.sender_id, # Тот кто начал (Крестики)
            "p2": opponent_id,        # Противник (Нолики)
            "p2_name": opponent_name,
            "msg_id": None
        }
        
        res = await self._draw(message, board, "❌", opponent_name)
        game_data["msg_id"] = res.id
        self.db.set("KrestikiPvP", "game", game_data)

    async def watcher(self, message):
        if not isinstance(message, Message) or not message.text:
            return
        
        game = self.db.get("KrestikiPvP", "game")
        if not game:
            return

        text = message.text.lower().strip()
        coords = {
            "1а": 0, "1б": 1, "1в": 2,
            "2а": 3, "2б": 4, "2в": 5,
            "3а": 6, "3б": 7, "3в": 8
        }

        if text in coords:
            # Проверка очереди
            current_player = game["p1"] if game["turn"] == "❌" else game["p2"]
            if message.sender_id != current_player:
                return

            idx = coords[text]
            board = game["board"]
            if board[idx] != "⬜️":
                return

            board[idx] = game["turn"]
            
            # Пытаемся удалить сообщение с ходом
            try: await message.delete()
            except: pass
            
            win = self._check(board)
            if win:
                await self._update(message, game, winner=game["turn"])
                self.db.set("KrestikiPvP", "game", None)
            elif "⬜️" not in board:
                await self._update(message, game, winner="draw")
                self.db.set("KrestikiPvP", "game", None)
            else:
                game["turn"] = "⭕️" if game["turn"] == "❌" else "❌"
                game["board"] = board
                self.db.set("KrestikiPvP", "game", game)
                await self._update(message, game)

    async def _update(self, message, game, winner=None):
        text = await self._draw(message, game["board"], game["turn"], game["p2_name"], winner, True)
        await self.client.edit_message(message.chat_id, game["msg_id"], text)

    async def _draw(self, message, b, turn, p2_name, winner=None, return_text=False):
        res = f"<b>Крестики-нолики 3x3</b>\n\n"
        res += f"   <b>А</b> <b>Б</b> <b>В</b>\n"
        res += f"<b>1</b> {b[0]} {b[1]} {b[2]}\n"
        res += f"<b>2</b> {b[3]} {b[4]} {b[5]}\n"
        res += f"<b>3</b> {b[6]} {b[7]} {b[8]}\n\n"
        
        if winner:
            res += f"<b>🏆 {'Ничья!' if winner == 'draw' else 'Победил: ' + winner}</b>"
        else:
            name = "Твой" if (turn == "❌") else p2_name
            res += f"<b>Ход: {turn} ({name})</b>\n<i>Пиши: 1а, 2б...</i>"
        
        if return_text: return res
        return await utils.answer(message, res)

    def _check(self, b):
        v = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
        return any(b[r[0]] == b[r[1]] == b[r[2]] != "⬜️" for r in v)
