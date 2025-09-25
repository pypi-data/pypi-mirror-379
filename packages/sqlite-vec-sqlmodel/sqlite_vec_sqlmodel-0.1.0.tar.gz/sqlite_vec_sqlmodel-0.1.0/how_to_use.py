from loguru import logger
import sqlite_vec
from sqlmodel import SQLModel, create_engine, Field, Session, Column
from sqlalchemy import event, select
from src.sqlite_vec_sqlalchemy import Vector, vec_distance_L2, vec_distance_cosine, enable_sqlite_vec

engine = create_engine("sqlite:///:memory:", echo=True)
enable_sqlite_vec(engine)

class BaseFAQ(SQLModel):
    id: int = Field(default=None, primary_key=True)
    question: str
    answer: str

class MyFAQ(BaseFAQ, table=True):
    embedding_q: list[float] = Field(sa_column=Column(Vector(3)))
    embedding_a: list[float] = Field(sa_column=Column(Vector(3)))

class FAQ(BaseFAQ):
    distance: float | None = None
    @classmethod
    def model_validate2(cls, data: tuple):
        faq, distance = data
        a = cls.model_validate(faq)
        a.distance = distance
        return a


def main() -> None:
    # 建表
    SQLModel.metadata.create_all(engine)

    # 插入示例数据（3 维向量）
    with Session(engine) as session:
        session.add_all([
            MyFAQ(
                question="alex",
                answer="A",
                embedding_q=[1.1, 1.1, 1.1],
                embedding_a=[1.1, 1.1, 1.1],
            ),
            MyFAQ(
                question="brian",
                answer="B",
                embedding_q=[2.2, 2.2, 2.2],
                embedding_a=[2.2, 2.2, 2.2],
            ),
            MyFAQ(
                question="craig",
                answer="C",
                embedding_q=[3.3, 3.3, 3.3],
                embedding_a=[3.3, 3.3, 3.3],
            ),
        ])
        session.commit()

    with Session(engine) as session:
        target = [2.2, 2.2, 2.1]  # also support str "[2.2, 2.2, 2.1]"
        distance_expr = vec_distance_L2(MyFAQ.embedding_q, target).label("distance")
        stmt = select(MyFAQ, distance_expr).order_by(distance_expr)
        res = session.exec(stmt).all()
        res2 = [FAQ.model_validate2(i) for i in res]
        logger.debug(res2)


if __name__ == "__main__":
    main()