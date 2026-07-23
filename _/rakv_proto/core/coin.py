from __future__ import annotations


class Coin:
    """
    王国币 (Kingdom Penny): 1GP = 12SP, 1SP = 20CP, 1GP = 240CP。

    Attributes:
        gp: 金币部分。
        sp: 银币部分。
        cp: 铜币部分。
        total_cp: 以铜币计的总价值。
    """

    __slots__ = ("_cp",)

    def __init__(self, gp: int = 0, sp: int = 0, cp: int = 0):
        """初始化货币，支持金币(GP)、银币(SP)、铜币(CP)混合输入。"""
        self._cp = gp * 240 + sp * 20 + cp

    @classmethod
    def from_cp(cls, total_cp: int) -> Coin:
        """从铜币总数创建 Coin 实例。"""
        c = cls.__new__(cls)
        c._cp = total_cp
        return c

    @property
    def gp(self) -> int:
        """返回金币部分。"""
        return self._cp // 240

    @property
    def sp(self) -> int:
        """返回银币部分。"""
        return (self._cp % 240) // 20

    @property
    def cp(self) -> int:
        """返回铜币部分。"""
        return self._cp % 20

    @property
    def total_cp(self) -> int:
        """返回以铜币计的总价值。"""
        return self._cp

    def __add__(self, other: Coin) -> Coin:
        """货币加法。"""
        if not isinstance(other, Coin):
            return NotImplemented
        return Coin.from_cp(self._cp + other._cp)

    def __sub__(self, other: Coin) -> Coin:
        """货币减法。"""
        if not isinstance(other, Coin):
            return NotImplemented
        return Coin.from_cp(self._cp - other._cp)

    def __mul__(self, scalar: int) -> Coin:
        """货币乘以整数倍数。"""
        if not isinstance(scalar, int):
            return NotImplemented
        return Coin.from_cp(self._cp * scalar)

    def __radd__(self, other: int | Coin) -> Coin:
        """反向加法，支持 sum() 聚合。"""
        if other == 0:
            return self
        if isinstance(other, Coin):
            return Coin.from_cp(other._cp + self._cp)
        return NotImplemented

    def __rmul__(self, scalar: int) -> Coin:
        """反向乘法。"""
        return self.__mul__(scalar)

    def __floordiv__(self, other: int | Coin) -> Coin | int:
        """整除：除以整数返回 Coin，除以 Coin 返回倍数。"""
        if isinstance(other, int):
            return Coin.from_cp(self._cp // other)
        if isinstance(other, Coin):
            return self._cp // other._cp
        return NotImplemented

    def __mod__(self, other: int) -> Coin:
        """取模运算。"""
        if not isinstance(other, int):
            return NotImplemented
        return Coin.from_cp(self._cp % other)

    def __neg__(self) -> Coin:
        """取负值。"""
        return Coin.from_cp(-self._cp)

    def __eq__(self, other: object) -> bool:
        """判断两个货币是否相等。"""
        if not isinstance(other, Coin):
            return NotImplemented
        return self._cp == other._cp

    def __lt__(self, other: Coin) -> bool:
        """小于比较。"""
        if not isinstance(other, Coin):
            return NotImplemented
        return self._cp < other._cp

    def __le__(self, other: Coin) -> bool:
        """小于等于比较。"""
        if not isinstance(other, Coin):
            return NotImplemented
        return self._cp <= other._cp

    def __gt__(self, other: Coin) -> bool:
        """大于比较。"""
        if not isinstance(other, Coin):
            return NotImplemented
        return self._cp > other._cp

    def __ge__(self, other: Coin) -> bool:
        """大于等于比较。"""
        if not isinstance(other, Coin):
            return NotImplemented
        return self._cp >= other._cp

    def __bool__(self) -> bool:
        """非零货币为 True。"""
        return self._cp != 0

    def __repr__(self) -> str:
        """返回调试用字符串表示。"""
        return f"Coin(gp={self.gp}, sp={self.sp}, cp={self.cp})"

    def __str__(self) -> str:
        """返回人类可读的货币字符串。"""
        parts = []
        if self.gp:
            parts.append(f"{self.gp}GP")
        if self.sp:
            parts.append(f"{self.sp}SP")
        if self.cp or not parts:
            parts.append(f"{self.cp}CP")
        return " ".join(parts)
