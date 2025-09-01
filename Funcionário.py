# Definindo a classe base Funcionario
class Funcionario:
    def __init__(self, nome, salario_base):
        """
        Construtor para a classe Funcionario.

        Args:
            nome (str): O nome do funcionário.
            salario_base (float): O salário base do funcionário.
        """
        self.nome = nome
        self.salario_base = salario_base

    def calcular_salario(self):
        """
        Calcula e retorna o salário do funcionário.
        """
        return self.salario_base

    def exibir_dados(self):
        """
        Imprime o nome e o salário do funcionário.
        """
        print(f"Nome: {self.nome}")
        print(f"Salário: R${self.calcular_salario():.2f}")

# Definindo a subclasse FuncionarioComissionado que herda de Funcionario
class FuncionarioComissionado(Funcionario):
    def __init__(self, nome, salario_base, comissao):
        """
        Construtor para a classe FuncionarioComissionado.

        Args:
            nome (str): O nome do funcionário.
            salario_base (float): O salário base do funcionário.
            comissao (float): O valor da comissão.
        """
        super().__init__(nome, salario_base)
        self.comissao = comissao

    def calcular_salario(self):
        """
        Sobrescreve o método calcular_salario() para incluir a comissão.
        """
        return self.salario_base + self.comissao

    def exibir_dados(self):
        """
        Sobrescreve o método exibir_dados() para incluir a comissão.
        """
        print(f"Nome: {self.nome}")
        print(f"Salário Base: R${self.salario_base:.2f}")
        print(f"Comissão: R${self.comissao:.2f}")
        print(f"Salário Total: R${self.calcular_salario():.2f}")

# Instanciando objetos das classes
funcionario_regular = Funcionario("João Silva", 3000.00)
funcionario_comissionado = FuncionarioComissionado("Maria Santos", 2500.00, 500.00)

# Exibindo os dados dos funcionários
print("--- Dados do Funcionário Regular ---")
funcionario_regular.exibir_dados()

print("\n--- Dados do Funcionário Comissionado ---")
funcionario_comissionado.exibir_dados()