from typing import List, Tuple, Iterable
import shapely
from shapely.geometry.base import BaseGeometry

from .definition import Shape, Single, Multi, NoParametersException, CoordinatesNotLegalException
from .impl_multi_complex import MultiComplexPolygon
from . import functional as F


class MultiSimplePolygon(MultiComplexPolygon):
    """
    多-单连通多边形, 创建方式有四:
    1. 指定 geo
    2. 指定 Multi
    3. 指定 Single 数组
    4. 指定 outers
    遵循逆序优先规则
    """

    __slots__ = ()

    def __init__(
            self,
            outers: List[Tuple[float, float]] = None,
            geo: BaseGeometry = None,
            shapes: Iterable[Shape] = None,
            from_p: List[Tuple[float, float]] = None,
            reverse: bool = False,
    ):
        if geo is not None:
            assert isinstance(geo, shapely.MultiPolygon), 'geo 必须是 MultiPolygon'
            assert all(g.boundary.geom_type.upper() == 'LINESTRING' for g in geo.geoms), 'geo 必须是单连通的'
        elif shapes is not None:
            assert all(isinstance(shape, (Single.SIMPLE, Multi.SIMPLE)) for shape in shapes if shape), 'shapes 必须由 SIMPLE（单连通） 图像构成'
        else:
            if from_p is not None:
                outers = from_p
            if outers is None:
                # 没有任何参数的话，要报个错
                raise NoParametersException(f'Any of such parameters have to be provided: (outer, *inners), geo, single, from_p')

            # 对用户输入进行检查和修复
            geo = shapely.MultiPolygon(polygons=[(outer, []) for outer in outers])
            geo = F.norm_geo(geo)
            # 创建时要求轮廓必须合法
            if geo is None:
                raise CoordinatesNotLegalException(f'creating single polygon with geo=={type(geo)}')
            elif isinstance(geo, shapely.Polygon):
                geo = shapely.MultiPolygon(polygons=[geo])
            # 还得是单连通的
            if any(g.interiors for g in geo.geoms):
                raise CoordinatesNotLegalException(f'MultiSimplePolygon not allowed interiors coordinates with geo interiors nums: {list(len(g.interiors) for g in geo.geoms)}')

        super().__init__(outers=None, geo=geo, shapes=shapes, reverse=reverse)

    # def merge(self, shape: Shape) -> Multi:
    #     # 合集运算
    #     geo = self.geo
    #     singles = shape.sep_out()
    #     geos = [s.geo for s in singles if not geo.disjoint(s.geo)]
    #     for g in geos:
    #         geo = geo.union(g)
    #     geo = self.__norm_multi__(geo)
    #     return ComplexMultiPolygon(geo=geo)

    @property
    def outer(self) -> Multi:
        # 外轮廓(正形)
        return Multi.SIMPLE(geo=self.geo)

    @property
    def inner(self) -> Shape.EMPTY:
        # 内轮廓(负形)
        return Shape.EMPTY

    def sep_in(self) -> Tuple[Multi, Shape.EMPTY]:
        # 内分解
        # 逐层分解 (规避由 shapely 的任意性引起的荒诞错误)
        return self, Shape.EMPTY

    def sep_out(self) -> List[Single]:
        # 外分解
        singles = [Single.SIMPLE(geo=g) for g in self.geo.geoms if isinstance(g, shapely.Polygon)]
        singles = [s for s in singles if s.is_valid()]
        return singles

    def sep_p(self) -> List[List[Tuple[int, int]]]:
        # 点分解
        # 逐层分解 (规避由 shapely 任意性引起的荒诞错误)
        singles = [Single.SIMPLE(geo=g) for g in self.geo.geoms if isinstance(g, shapely.Polygon)]
        singles = [s for s in singles if s.is_valid()]
        return [s.sep_p() for s in singles if s.is_valid()]

    @property
    def cls(self) -> type:
        return MultiSimplePolygon


Multi.SIMPLE = MultiSimplePolygon
