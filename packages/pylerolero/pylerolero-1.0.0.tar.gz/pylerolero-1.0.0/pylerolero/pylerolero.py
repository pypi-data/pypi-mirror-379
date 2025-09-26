# IMPORTAÇÕES:
import random
import hashlib
import json

'''

'''
class PyLeroLero:
    def __init__(self):
        '''
        SEGMENTO 1 DA FRASE:
            Os [adjuntos] servem como um adjunto adverbial de início de frase ou conectivo.
            Eles estabelecem a ligação lógica da frase com o que a precede, indicando uma
            relação de oposição ("No entanto"), tempo ("Pensando mais a longo prazo"),
            causa/consequência ("Por conseguinte") ou simplesmente introduzindo o
            assunto ("Caros amigos,").
        '''
        self.adjuntos = [
            "Caros amigos, ",
            "Por outro lado, ",
            "Assim mesmo, ",
            "No entanto, não podemos esquecer que ",
            "Do mesmo modo, ",
            "A prática cotidiana prova que ",
            "Nunca é demais lembrar o peso e o significado destes problemas, uma vez que ",
            "As experiências acumuladas demonstram que ",
            "Acima de tudo, é fundamental ressaltar que ",
            "O incentivo ao avanço tecnológico, assim como ",
            "Não obstante, ",
            "Todas estas questões, devidamente ponderadas, levantam dúvidas sobre se ",
            "Pensando mais a longo prazo, ",
            "O que temos que ter sempre em mente é que ",
            "Ainda assim, existem dúvidas a respeito de como ",
            "Gostaria de enfatizar que ",
            "Todavia, ",
            "A nível organizacional, ",
            "O empenho em analisar ",
            "Percebemos, cada vez mais, que ",
            "No mundo atual, ",
            "É importante questionar o quanto ",
            "Neste sentido, ",
            "Evidentemente, ",
            "Por conseguinte, ",
            "É claro que ",
            "Podemos já vislumbrar o modo pelo qual ",
            "Desta maneira, ",
            "O cuidado em identificar pontos críticos n",
            "A certificação de metodologias que nos auxiliam a lidar com "
        ]
        '''
        SEGMENTO 2 DA FRASE:
            Os [sujeitos] são o sujeito da oração. Geralmente, eles são compostos por um
            substantivo ou uma expressão substantivada (como "a execução dos pontos do
            programa") que realiza a ação expressa pelo verbo. É o "quem" ou "o que"
            da frase.
        '''
        self.sujeitos = [
            "a execução dos pontos do programa ",
            "a complexidade dos estudos efetuados ",
            "a contínua expansão de nossa atividade ",
            "a estrutura atual da organização ",
            "o novo modelo estrutural aqui preconizado ",
            "o desenvolvimento contínuo de distintas formas de atuação ",
            "a constante divulgação das informações ",
            "a consolidação das estruturas ",
            "a consulta aos diversos militantes ",
            "o início da atividade geral de formação de atitudes ",
            "o desafiador cenário globalizado ",
            "a mobilidade dos capitais internacionais ",
            "o fenômeno da Internet ",
            "a hegemonia do ambiente político ",
            "a expansão dos mercados mundiais ",
            "o aumento do diálogo entre os diferentes setores produtivos ",
            "a crescente influência da mídia ",
            "a necessidade de renovação processual ",
            "a competitividade nas transações comerciais ",
            "o surgimento do comércio virtual ",
            "a revolução dos costumes ",
            "o acompanhamento das preferências de consumo ",
            "o comprometimento entre as equipes ",
            "a determinação clara de objetivos ",
            "a adoção de políticas descentralizadoras ",
            "a valorização de fatores subjetivos ",
            "a percepção das dificuldades ",
            "o entendimento das metas propostas ",
            "o consenso sobre a necessidade de qualificação ",
            "o julgamento imparcial das eventualidades "
        ]
        '''
        SEGMENTO 3 DA FRASE:
            Os [verbos] são o verbo da oração, acompanhado, na maioria dos casos, de um
            complemento verbal (como "nos obriga à análise"). Eles expressam a ação,
            estado ou fenômeno realizado pelo sujeito. É o coração da frase, que
            indica o que está acontecendo.
        '''
        self.verbos = [
            "nos obriga à análise ",
            "cumpre um papel essencial na formulação ",
            "exige a precisão e a definição ",
            "auxilia a preparação e a composição ",
            "garante a contribuição de um grupo importante na determinação ",
            "assume importantes posições no estabelecimento ",
            "facilita a criação ",
            "obstaculiza a apreciação da importância ",
            "oferece uma interessante oportunidade para verificação ",
            "acarreta um processo de reformulação e modernização ",
            "pode nos levar a considerar a reestruturação ",
            "representa uma abertura para a melhoria ",
            "ainda não demonstrou convincentemente que vai participar na mudança ",
            "talvez venha a ressaltar a relatividade ",
            "prepara-nos para enfrentar situações atípicas decorrentes ",
            "maximiza as possibilidades por conta ",
            "desafia a capacidade de equalização ",
            "agrega valor ao estabelecimento ",
            "é uma das consequências ",
            "promove a alavancagem ",
            "não pode mais se dissociar ",
            "possibilita uma melhor visão global ",
            "estimula a padronização ",
            "aponta para a melhoria ",
            "faz parte de um processo de gerenciamento ",
            "causa impacto indireto na reavaliação ",
            "apresenta tendências no sentido de aprovar a manutenção ",
            "estende o alcance e a importância ",
            "deve passar por modificações independentemente ",
            "afeta positivamente a correta previsão "
        ]
        '''
        SEGMENTO 4 DA FRASE:
            Os [complementos] funcionam como o complemento do complemento verbal (adjunto
            adverbial ou complemento nominal) dos verbos. Eles complementam o sentido do
            verbo e da expressão anterior, detalhando a ação, a análise,
            a formulação, etc. Geralmente, são introduzidos por uma preposição
            (como "das condições", "do sistema") e especificam sobre o que a ação
            do verbo se refere.
        '''
        self.complementos = [
            "das condições financeiras e administrativas exigidas.",
            "das diretrizes de desenvolvimento para o futuro.",
            "do sistema de participação geral.",
            "das posturas dos órgãos dirigentes com relação às suas atribuições.",
            "das novas proposições.",
            "das direções preferenciais no sentido do progresso.",
            "do sistema de formação de quadros que corresponde às necessidades.",
            "das condições inegavelmente apropriadas.",
            "dos índices pretendidos.",
            "das formas de ação.",
            "dos paradigmas corporativos.",
            "dos relacionamentos verticais entre as hierarquias.",
            "do processo de comunicação como um todo.",
            "dos métodos utilizados na avaliação de resultados.",
            "de todos os recursos funcionais envolvidos.",
            "dos níveis de motivação departamental.",
            "da gestão inovadora da qual fazemos parte.",
            "dos modos de operação convencionais.",
            "de alternativas às soluções ortodoxas.",
            "dos procedimentos normalmente adotados.",
            "dos conhecimentos estratégicos para atingir a excelência.",
            "do fluxo de informações.",
            "do levantamento das variáveis envolvidas.",
            "das diversas correntes de pensamento.",
            "do impacto na agilidade decisória.",
            "das regras de conduta normativas.",
            "do orçamento setorial.",
            "do retorno esperado a longo prazo.",
            "do investimento em reciclagem técnica.",
            "do remanejamento dos quadros funcionais."
        ]

    """
        Configura uma semente para as funções randômicas.

        Args:
            seed (any): Valor que será utilizado como semente nas funções de
                randomização.

        Returns:
            int: A semente que foi configurada.
    """
    def set_seed(self, seed=None):
        
        # Uma semente foi fornecida pelo usuário:
        if seed:
            hash_object = hashlib.sha256(str(seed).encode())
            seed_value = int(hash_object.hexdigest(), 16)
        
        # Randomiza uma semente caso o usuário não forneça uma:
        else:
            seed_value = random.randint(0,99999)
        
        # Configura a semente gerada:
        random.seed(seed_value)
            
        # Retorna a semente que foi configurada.
        return seed_value
    
    '''
        Injetando novos segmentos para personalizar a geração de frases,
        parágrafos e textos.
        
        Args:
            injection (json): JSON contendo o modo desejado e as listas de
                termos para cada segmento.
            
        Returns:
            json: Retorna um JSON com o resultado final dos segmentos
                após a injeção.
    '''
    def inject(self, injection=None):
        
        # Injeta os segmentos recebidos:
        if injection:
            
            # Injeta de acordo com o modo desejado:
            if injection.get("mode"):
                
                # Verifica a existência de segmentos:
                if injection.get("segments"):
                
                    # Adiciona os segmentos recebidos aos segmentos atuais:
                    if injection["mode"] == "append":
                        if injection["segments"].get("adjuntos") and isinstance(injection["segments"]["adjuntos"], list):
                            self.adjuntos = list(set(self.adjuntos + injection["segments"]["adjuntos"]))
                        if injection["segments"].get("sujeitos") and isinstance(injection["segments"]["sujeitos"], list):
                            self.sujeitos = list(set(self.sujeitos + injection["segments"]["sujeitos"]))
                        if injection["segments"].get("verbos") and isinstance(injection["segments"]["verbos"], list):
                            self.verbos = list(set(self.verbos + injection["segments"]["verbos"]))
                        if injection["segments"].get("complementos") and isinstance(injection["segments"]["complementos"], list):
                            self.complementos = list(set(self.complementos + injection["segments"]["complementos"]))
                    
                    # Substitui os segmentos atuais pelos segmentos recebidos:
                    elif injection["mode"] == "replace":
                        if injection["segments"].get("adjuntos") and isinstance(injection["segments"]["adjuntos"], list):
                            self.adjuntos = injection["segments"]["adjuntos"]
                        if injection["segments"].get("sujeitos") and isinstance(injection["segments"]["sujeitos"], list):
                            self.sujeitos = injection["segments"]["sujeitos"]
                        if injection["segments"].get("verbos") and isinstance(injection["segments"]["verbos"], list):
                            self.verbos = injection["segments"]["verbos"]
                        if injection["segments"].get("complementos") and isinstance(injection["segments"]["complementos"], list):
                            self.complementos = injection["segments"]["complementos"]
                        
                    # Modo de injeção inválido:
                    else:
                        return_json = {
                            "erro": "Modo de injeção inválido."
                        }
                        return json.dumps(return_json, ensure_ascii=False, indent=4)
                    
                    return_json = {
                        "mode": "injected",
                        "segments": {
                            "adjuntos": self.adjuntos,
                            "sujeitos": self.sujeitos,
                            "verbos": self.verbos,
                            "complementos": self.complementos,
                        }
                    }
                    return json.dumps(return_json, ensure_ascii=False, indent=4)
            
            # O modo padrão é "replace":
            else:
                return_json = {
                    "erro": "Modo de injeção não encontrado."
                }
                return json.dumps(return_json, ensure_ascii=False, indent=4)
                
        # O JSON de injeção é obrigatório:
        else:
            return_json = {
                "erro": "Nenhum JSON de injeção encontrado."
            }
            return json.dumps(return_json, ensure_ascii=False, indent=4)
    
    """
        Gerando uma frase a partir de uma semente.

        Args:
            seed (any, opcional): Valor que será utilizado como semente nas funções de
                randomização durante a geração da frase. (Padrão: None).

        Returns:
            string: A frase gerada pela concatenação de um elemento de cada
                lista de segmento.
    """
    def generate_phrase(self, seed=None):
        
        # Configura a semente de randomização:
        self.set_seed(seed)
        
        # Gera e retorna a frase a partir da semente de randomização definida:
        return random.choice(self.adjuntos) + random.choice(self.sujeitos) + random.choice(self.verbos) + random.choice(self.complementos)

    """
        Gerando um parágrafo de um tamanho específico a partir de uma semente.

        Args:
            density (int, opcional): Densidade do parágrafo em quantidade de frases.
                (Padrão: 3).
            seed (any, opcional): Valor que será utilizado como semente nas funções de
                randomização durante a geração do parágrafo. (Padrão: None).

        Returns:
            string: O parágrafo gerado pela concatenação das frases geradas.
    """
    def generate_paragraph(self, density=3, seed=None):
        
        # Configura a semente de randomização:
        self.set_seed(seed)
        
        # Armazenamento das frases geradas:
        phrases = []
        
        # Gera a quantidade de frases desejadas:
        for _ in range(density):
            phrases.append(self.generate_phrase(random.randint(0,99999)))
            
        # Agrega as frases e retorna o parágrafo gerado:
        return " ".join(phrases)

    """
        Gerando um texto de um tamanho específico a partir de uma semente.

        Args:
            size (int, opcional): Tamanho do texto em quantidade de parágrafos.
                (Padrão: 3).
            density (int, opcional): Tamanho dos parágrafos que compõe o texto.
                (Padrão: 3).
            seed (any, opcional): Valor que será utilizado como semente nas funções de
                randomização durante a geração do texto. (Padrão: None).

        Returns:
            string: O texto gerado pela concatenação dos parágrafos gerados.
    """
    def generate_text(self, size=3, density=3, seed=None):
        
        # Configura a semente de randomização:
        self.set_seed(seed)
        
        # Armazenamento das frases geradas:
        paragraphs = []
        
        # Gera a quantidade de frases desejadas:
        for _ in range(size):
            paragraphs.append(self.generate_paragraph(density, random.randint(0,99999)))
            
        # Agrega as frases e retorna o parágrafo gerado:
        return "\n\n".join(paragraphs)