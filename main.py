from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from tables import Refeicao, Base, Comidas
import dotenv
import os


dotenv.load_dotenv()
db_password = os.getenv('DB_PASSWORD')

engine = create_engine(f'postgresql://postgres:{db_password}@127.0.0.1:5432/alimentos')
Base.metadata.create_all(engine)

with Session(engine) as session:
    o_que_comeu = input('O que você comeu? ').split(sep=',')

    results = []
    for alimento in o_que_comeu:
        querys = session.query(Comidas).filter(Comidas.nome_alimento.like(f'%{alimento}%')).all()
        if len(querys) > 1:
            for index, result in enumerate(querys):
               print(f'[ {index} ] {result.nome_alimento} feito {result.preparo}')
            variavel = int(input('Qual o número correspondente ao que tu comestes? '))
            results.append(querys[variavel])
        else:
           results.append(querys[0])

    total_kcal = [result.kcal for result in results]
    somatoria = sum(total_kcal)
    test = [result.nome_alimento for result in results]
    comidas = ", ".join(test)

    refeicao = Refeicao( 
        data_horario = datetime.now(), 
        comidas = comidas,
        total_caloria = somatoria,
    )
         
    session.add_all([refeicao])

    session.commit()

