import json, oracledb, os

def ler_inteiro(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            if valor <= 0:
                print("O valor deve ser maior que zero.")
                continue
            return valor
        except ValueError:
            print("Erro: Por favor, digite apenas números inteiros.")
        
def ler_float(mensagem):
    while True:
        try:
            valor = float(input(mensagem).replace(',', '.'))
            if valor < 0:
                print("O valor não pode ser negativo.")
                continue
            return valor
        except ValueError:
            print("Erro: Por favor, digite um número válido.")

def ler_tipo_colheita():
    while True:
        tipo = input("Tipo de colheita (M - Mecanizada / A - Manual): ").strip().upper()
        if tipo in ['M', 'A']:
            return "Mecanizada" if tipo == 'M' else "Manual"
        print("Erro: Digite 'M' para Mecanizada ou 'A' para Manual.")

def calcular_perdas(prod_esperada, prod_real, tipo_colheita):
    if prod_esperada == 0:
         return (0.0, "Erro: Esperada zerada")
    perda = ((prod_esperada - prod_real) / prod_esperada) * 100
    # Lógica baseada no texto (Manual aceita até 5%, Mecanizada até 15%)
    limite = 15.0 if tipo_colheita == "Mecanizada" else 5.0
    
    if perda <= 0:
        status = "Excelente (Acima da meta)"
    elif perda <= limite:
        status = "Normal (Dentro da margem)"
    else:
        status = "Crítico (Revisar planejamento/máquinas!)"
        
    return (round(perda, 2), status) # Retornando uma Tupla
  
def cadastrar_talhao(tabela_memoria):
    print("\n---REGISTRO DE COLHEITA---")
    id_talhao = ler_inteiro("Número de identificação do Talhão (Lote): ")
    tipo = ler_tipo_colheita()
    esperada = ler_float("Produção esperada (Toneladas): ")
    real = ler_float("Produção real colhida (Toneladas): ")
    
    perda_perc, status = calcular_perdas(esperada, real, tipo)
    
    registro = {
        "id_talhao": id_talhao,
        "tipo_colheita": tipo,
        "producao_esperada": esperada,
        "producao_real": real,
        "perda_percentual": perda_perc,
        "status": status
    }
    
    tabela_memoria.append(registro)
    print("\nRegistro salvo na memória com sucesso!")
    print(f"Resultado: Perda de {perda_perc}% -> {status}")

def salvar_em_arquivos(tabela_memoria):
    """Manipulação de Arquivos: Salva em JSON (Dados estruturados) e TXT (Relatório)."""
    if not tabela_memoria:
        print("\nNão há dados na memória para salvar.")
        return
    try:
        with open("dados_colheita.json", "w", encoding="utf-8") as f:
            json.dump(tabela_memoria, f, ensure_ascii=False, indent=4)
        print("\nBase de dados salva em 'dados_colheita.json'.")
    except Exception as e:
        print(f"Erro ao salvar JSON: {e}")

    # Salvando Relatório TXT
    try:
        with open("relatorio_colheita.txt", "w", encoding="utf-8") as f:
            f.write("="*40 + "\n")
            f.write("RELATÓRIO DE PERDAS - CANATECH\n")
            f.write("="*40 + "\n")
            for item in tabela_memoria:
                f.write(f"Talhão: {item['id_talhao']} | Tipo: {item['tipo_colheita']}\n")
                f.write(f"Perda: {item['perda_percentual']}% | Status: {item['status']}\n")
                f.write("-" * 40 + "\n")
        print("Relatório gerado em 'relatorio_colheita.txt'.")
    except Exception as e:
        print(f"Erro ao gerar TXT: {e}")

# Integração com Banco Oracle
def exportar_para_oracle(tabela_memoria):
    if not tabela_memoria:
        print("\nNão há dados para enviar.")
        return
    print("\nConectando ao Banco de Dados Oracle...")
    try:
        connection = oracledb.connect(user=USER, password=PASS, dsn=DSN)
        cursor = connection.cursor()
        sucessos = 0
        for item in tabela_memoria:
            try:
                # Instrução SQL parametrizada
                sql = """INSERT INTO TAB_COLHEITA_CANA 
                         (ID_TALHAO, TIPO_COLHEITA, PROD_ESPERADA, PROD_REAL, PERDA_PERC, STATUS) 
                         VALUES (:1, :2, :3, :4, :5, :6)"""
                
                dados = (item['id_talhao'], item['tipo_colheita'], item['producao_esperada'], 
                         item['producao_real'], item['perda_percentual'], item['status'])
                
                cursor.execute(sql, dados)
                sucessos += 1
            except oracledb.IntegrityError:
                print(f"Talhão {item['id_talhao']} já existe no banco e foi ignorado.")
            except Exception as e:
                print(f"Erro ao inserir talhão {item['id_talhao']}: {e}")

        connection.commit()
        cursor.close()
        connection.close()
        print(f"{sucessos} registros exportados para o Oracle com sucesso!")
        
    except Exception as e:
        print(f"Falha de conexão com o banco de dados: {e}")
        print("Verifique se as credenciais (USER, PASS, DSN) estão configuradas corretamente.")

def main():
    # Estrutura de Dados: Lista (servirá como Tabela de Memória)
    tabela_memoria = [] 
    
    while True:
        print("\n" + "="*40)
        print("GESTÃO DE COLHEITA")
        print("="*40)
        print("1. Registrar Colheita de Talhão")
        print("2. Exibir Registros (Memória)")
        print("3. Gerar Arquivos (JSON e TXT)")
        print("4. Sincronizar com Oracle DB")
        print("0. Sair do Sistema")
        print("="*40)
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            cadastrar_talhao(tabela_memoria)
        elif opcao == '2':
            if not tabela_memoria:
                print("\nNenhum dado registrado na memória no momento.")
            else:
                print("\n---REGISTROS ATUAIS---")
                for item in tabela_memoria:
                    # Usabilidade: Saída limpa no console
                    print(f"Lote {item['id_talhao']:04d} | {item['tipo_colheita'][:3]} | Perda: {item['perda_percentual']}% | {item['status']}")
        elif opcao == '3':
            salvar_em_arquivos(tabela_memoria)
        elif opcao == '4':
            exportar_para_oracle(tabela_memoria)
        elif opcao == '0':
            print("\nEncerrando o CanaTech Monitor. Até logo!")
            break
        else:
            print("\nOpção inválida! Tente novamente.")
          
if __name__ == "__main__":
    main()
  
