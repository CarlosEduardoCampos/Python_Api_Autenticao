# pip install sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, TIMESTAMP, text
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///atividades.db')

db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


class Pessoas(Base):
    __tablename__ = 'pessoas'
    id = Column(Integer, primary_key=True)
    nome = Column(String(40), index=True)
    idade = Column(Integer)

    def __repr__(self):
        return f'< Pessoa -> {self.nome} >'

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()


class Usuarios(Base):
    __tablename__='usuarios'
    id = Column(Integer, primary_key=True)
    nivel = Column(Integer)
    login = Column(String(40), unique=True)
    senha = Column(String(300))
    pessoa_id = Column(Integer, ForeignKey('pessoas.id'))
    pessoa = relationship("Pessoas")

    def __repr__(self):
        return f'< Login -> {self.login} >'

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()


class Atividades(Base):
    __tablename__ = 'atividades'
    id = Column(Integer, primary_key=True)
    titulo = Column(String(80))
    pessoa_id = Column(Integer, ForeignKey('pessoas.id'))
    pessoa = relationship("Pessoas")

    def __repr__(self):
        return f'< Atividade -> {self.titulo} >'

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()


def init_db():
    Base.metadata.create_all(bind=engine)


def delete_db():
    Base.metadata.delete_all(bind=engine)


if __name__ == '__main__':
    init_db()

