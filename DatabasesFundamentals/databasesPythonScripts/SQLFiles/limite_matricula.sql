CREATE OR REPLACE FUNCTION verificar_capacidade_turma()
RETURNS TRIGGER AS $$
BEGIN
    IF (SELECT COUNT(*) FROM Aluno_Turma WHERE turma_id = NEW.turma_id) >=
       (SELECT capacidade_maxima FROM Turma WHERE id = NEW.turma_id) THEN
        RAISE EXCEPTION 'A capacidade máxima da turma foi atingida!';
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;