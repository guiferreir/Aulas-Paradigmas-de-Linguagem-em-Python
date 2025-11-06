from sistema_emprestimos.equipamento import Equipamento
from sistema_emprestimos.usuario import Usuario
from sistema_emprestimos.emprestimo import Emprestimo
from sistema_emprestimos.inventario import Inventario
from sistema_emprestimos.registro_auditoria import RegistroAuditoria

if __name__ == "__main__":
    inv = Inventario()
    audit = RegistroAuditoria()

##testes
    eq1 = Equipamento("E001", "Laptop", "2023-03-10")
    inv.adicionar_equipamento(eq1)

    eq2 = Equipamento("E002", "Tablet", "2022-06-15")
    inv.adicionar_equipamento(eq2)

    user1 = Usuario("U001", "Maria Silva", "aluno")

    emp1 = Emprestimo("EMP001", user1, eq1, "2025-12-01")
    audit.registrar("Empréstimo criado", user1)

    try:
        Emprestimo("EMP002", user1, eq2, "2025-12-01")
    except ValueError as e:
        print("Erro esperado:", e)

    emp1.encerrar()
    audit.registrar("Empréstimo encerrado", user1)

    print("\nRegistro de Auditoria:")
    for log in audit.entradas:
        print(log)

    print("\nEquipamentos disponíveis:")
    for eq in inv.listar_disponiveis():
        print(f"- {eq.id_equipamento}: {eq.tipo} ({eq.estado})")
