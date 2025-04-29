import psycopg

with psycopg.connect("host=200.129.44.249 port=5432 dbname=540311 user=540311 password=540311") as conn:
    
    with conn.cursor() as cur:

        cur.execute("""
                SELECT * FROM Turma
                """)
        
        print("Turmas:")
        for row in cur.fetchall():
            print(row)
        
        cur.execute("""
                SELECT turma_id, COUNT (aluno_id)
                FROM Aluno_Turma
                GROUP BY turma_id
                ORDER BY turma_id ASC
                """)

        print("\nQuantidade de alunos por turma:")
        for row in cur.fetchall():
            turma_id, alunos_count = row
            print(f"Quantidade de alunos na turma {turma_id}: {alunos_count}")
        
        conn.commit()