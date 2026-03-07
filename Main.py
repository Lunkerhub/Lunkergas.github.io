# meta developer: @Honorpadx9lte

from .. import loader, utils
from telethon.tl.types import Message

@loader.tds
class TicTacToeMod(loader.Module):
    """Крестики-нолики 3x3 на кнопках"""
    strings = {"name": "KrestikiNoliki"}

    async def krestcmd(self, message: Message):
        """Запустить игру 3x3"""
        board = [" " for _ in range(9)]
        await self._render(message, board, "❌")

    async def _render(self, message, board, turn, winner=None):
        kb = []
        for i in range(0, 9, 3):
            row = []
            for j in range(3):
                idx = i + j
                char = board[idx]
                row.append({
                    "text": char if char != " " else "⬜️",
                    "callback": self._click,
                    "args": (board, idx, turn)
                })
            kb.append(row)

        status = f"Ход: {turn}"
        if winner:
            status = "🤝 Ничья!" if winner == "draw" else f"🏆 Победил: {winner}"
        
        await self.inline.form(
            text=f"<b>Игра: Крестики-нолики</b>\n{status}",
            message=message,
            controls=[[{"text": "🔄 Рестарт", "callback": self.krestcmd}]],
            reply_markup=kb
        )

    async def _click(self, call, board, idx, turn):
        if board[idx] != " " or self._check(board):
            return await call.answer("Игра завершена или клетка занята!")

        board[idx] = turn
        win = self._check(board)
        
        if win:
            await self._render(call.message, board, turn, winner=turn)
        elif " " not in board:
            await self._render(call.message, board, turn, winner="draw")
        else:
            next_turn = "⭕️" if turn == "❌" else "❌"
            await self._render(call.message, board, next_turn)
        await call.answer()

    def _check(self, b):
        v = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
        for r in v:
            if b[r[0]] == b[r[1]] == b[r[2]] != " ":
                return True
        return False
