def custom_split(word):
    return [char for char in str(word)]

# Check
def algoritimo_luhn(number):

    # pegando o valor passado por parâmetro e forçando ser string
    number = str(number).replace(" ", "")

    # vetor de dígitos numéricos do number passado por parâmetro
    vector_numbers = [x for x in custom_split(number)]
    
    # armazenamento dos valores processados
    new_numbers = []

    # variável auxiliar para criar um
    cursor = 0

    # soma total dos elementos de new_numbers
    checksum = 0

    # percorrendo os valores do vetor dos digitos do numeros
    for current_number in vector_numbers:

        # verifica se o modulo do cursor por 2 é igual a 0 
        # se for será multiplicaodo valor daquele numero para 2
        if cursor % 2 == 0:

            # multiplicando o numero atual por 2
            current_number = int(current_number)*2

            # verificar se o tamanho do numero é de 2 digitos
            # se for temos que somar os digitos individualmente
            # exemplo: 12 -> 1 + 2 = 3, o tres sera o valor do current_number
            if current_number > 9:
                # quebrando o numero atual de dois digitos para somar cada parcela
                splited_current_number = [int(x) for x in custom_split(current_number)]
                
                # zerando o valor do numero atual
                current_number=0

                # somando os numeros individulamente
                for p in splited_current_number:
                    current_number = current_number+p
        
        # após o processo de calculo dos número em determinado índice será adicionado ao vetor
        # new_numbers
        new_numbers.append(current_number)
        
        # o cursor aumenta +1
        cursor=cursor+1
    
    # soma de todos os elementos que foram adicionados em new_numbers
    for x in new_numbers:
        checksum = checksum+int(x)
    
    # retorna true se a variavel checksum é mod de 10 e falso para o contrário.
    return ((checksum % 10) == 0)

cartao_test = 5090697854632091
print("[LOG] {cartao} é valido? (true/false): {result}".format(cartao=cartao_test, result=algoritimo_luhn(cartao_test)))
