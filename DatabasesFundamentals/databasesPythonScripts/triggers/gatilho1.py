import psycopg

with psycopg.connect("host=200.129.44.249 port=5432 dbname=540311 user=540311 password=540311") as conn:
    
    with conn.cursor() as cur:

        cur.executemany("""
            INSERT INTO Aluno_Turma (aluno_id, turma_id)
            VALUES (%s, %s);
            """,
            [
                (3, 1),
                (5, 1),
                (4, 1),
            ]
            )
        
        conn.commit()