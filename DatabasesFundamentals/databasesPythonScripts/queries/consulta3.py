import psycopg

with psycopg.connect("host=200.129.44.249 port=5432 dbname=540311 user=540311 password=540311") as conn:
    
    with conn.cursor() as cur:

        cur.execute("""
                SELECT id
                FROM Curso
                WHERE nome = 'Ciências da Computação'
                """)
        curso_id = cur.fetchone()[0]

        cur.execute("""
                SELECT COUNT (id)
                FROM Professor
                WHERE curso_id = %s
                """,
                (curso_id,))
        quant_professores = cur.fetchone()[0]

        print(f"Número de professores no curso de Ciência da Computação: {quant_professores}")

        conn.commit()