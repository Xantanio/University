import psycopg

with psycopg.connect("host=200.129.44.249 port=5432 dbname=540311 user=540311 password=540311") as conn:
    
    with conn.cursor() as cur:

        cur.execute("""
                SELECT curso_id
                FROM Disciplina
                WHERE nome = 'Fundamentos de Bancos de Dados'
                """)
        curso_id = cur.fetchone()[0]
        
        cur.execute("""
                SELECT nome
                FROM Aluno
                WHERE curso_id = %s
                """,
                (curso_id,))
        
        print(f"Alunos matriculados na disciplina de Fundamentos de Bancos de Dados:")
        for row in cur.fetchall():
            print(f"{row[0]}")
        
        conn.commit()