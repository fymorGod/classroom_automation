from selenium.webdriver.common.by import By
from lib import Lib
from time import sleep

class TestsPage(Lib):
    'Coloquem os localizadores dos elementos aqui, vai facilitar!'
    URL = 'https://undbclassroom.undb.edu.br'
    __LOGIN_DIRETO_URL = 'https://undbclassroom.undb.edu.br/login/index.php#'
    __URL_ICON = 'https://cdn-icons-png.flaticon.com/512/1521/1521260.png'
    __EMAIL_TEXTBOX =  By.ID, 'username'
    __SENHA_TEXTBOX = By.ID, 'password'
    __ACESSAR_BUTTON = By.CLASS_NAME, 'btn-primary'
    __ESQUECEU_SENHA_BUTTON = By.XPATH, '//a[contains(text(), "Esqueceu o seu usuário ou senha?")]'
    __ID_USUARIO_TEXTBOX = By.ID, 'id_username'
    __BUSCAR_BUTTON = By.NAME, 'submitbuttonusername'
    __ID_EMAIL_TEXTBOX = By.ID, 'id_email'
    __ACESSAR_TEIA = By.XPATH, '//*[@id="page"]/div[2]/div/div/div[1]/div/a'
    __ACESSAR_PORTAL = By.XPATH, '//*[@id="page"]/div[2]/div/div/div[2]/div/a'
    __ACESSAR_SITE = By.XPATH, '//*[@id="page"]/div[2]/div/div/div[3]/div/a'
    __LEMBRAR_USUARIO = By.NAME, "rememberusername"
    __ACESSAR_LINK_PLAYSTORE = By.XPATH, '//*[@id="top-footer"]/div/div/div[1]/h4/a[1]/img'
    __CALENDARIO = By.XPATH, '//*[@id="nav-drawer"]/ul/li[3]/a'
    __SETA_CALENDARIO = By.CLASS_NAME, 'arrow_text'
    __ACESSAR_LINK_APPSTORE = By.XPATH, '//*[@id="top-footer"]/div/div/div[1]/h4/a[2]/img'
    __ACESSAR_EMAIL_INSTITUCIONAL = By.XPATH, '//*[@id="boxForm"]/div/div/div/a'
    __ACESSAR_BARRA_OPCOES = By.XPATH, '//*[@id="action-menu-toggle-1"]'
    __ACESSSAR_SAIR = By.XPATH, '//*[@id="action-menu-1-menu"]/a[7]'
    __EMAIL_GOOGLE = By.ID, 'identifierId'
    __BOTAO_PROXIMO = By.XPATH, '//*[@id="identifierNext"]/div/button'
    __DISCIPLINA_TESTAGEM = By.XPATH, '//*[@id="frontpage-course-list"]/div/div[1]/div[2]/div[3]/div/a'
    __CLICK_SARAIVA = By.XPATH, '//*[@id="module-120666"]/div/div/div[2]/div/a'
    __CLICK_PEARSON = By.XPATH, '//*[@id="module-120667"]/div/div/div[2]/div'
    __EMAIL_NAV = By.CLASS_NAME, 'fa-envelope'
    __NEW_EMAIL = By.CLASS_NAME, 'mail-navbar-menu-compose-link'
    __SEND_EMAIL = By.NAME, 'send'
    __ERROR_DESTINATARIO = By.ID, 'id_error_recipients'
    __PESQUISA_SATISFACAO = By.XPATH, '//*[@id="module-120665"]/div/div/div[2]/div/a/span'
    __RESPONDA_PESQUISA = By.XPATH, '//*[@id="region-main"]/div[1]/div/div/div[2]/div/a'
    __SIM_BUTTTON = By.ID, 'id_multichoice_16594_1'
    __NAO_BUTTTON = By.ID, 'id_multichoice_16594_2'
    __NOTIFICACOES = By.CLASS_NAME, 'slicon-bell'
    __PREFERENCIAS_NOTIFICACOES = By.CLASS_NAME, 'slicon-settings'
    __NOTIFICAO_WEB = By.CLASS_NAME, 'preference-state-status-container'
    __AV_QUALIS = By.XPATH, '//span[contains(text(), "Av Qualis - Produto")]'
    __ADICIONAR_ENVIO = By.XPATH, '//button[contains(text(), "Adicionar envio")]'
    __SALVAR_ENVIO = By.NAME, 'submitbutton'
    __ALERTA_ENVIO = By.CLASS_NAME, 'alert-danger'
    __PERFIL_USER = By.XPATH, '//*[@id="action-menu-toggle-1"]/span/span[2]/span/img'
    __PREFERENCIAS_USER = By.XPATH, '//*[@id="action-menu-1-menu"]/a[6]'
    __MODIFICAR_PERFIL = By.XPATH, '//*[@id="region-main"]/div/div/div/div/div[1]/div/div/div/div[1]/a'
    __SOLTAR_IMAGEM = By.CLASS_NAME, 'dndupload-arrow'
    __UTILIZAR_URL = By.XPATH, '//span[contains(text(), "Utilizar uma URL")]'
    __DOWNLOAD_IMAGE = By.CLASS_NAME, 'fp-login-submit'
    __IMAGEM = By.CLASS_NAME, 'fp-reficons2'
    __FILL_URL = By.XPATH, '//input[@id="fileurl"]'
    __ATV__TESTAGEM = By.XPATH, '//*[@id="module-122898"]/div/div/div[2]/div/a/span'
    __TEST_SEND_AGAIN = By.XPATH, '//*[@id="yui_3_17_2_1_1632675935201_861"]/a[1]/div[1]/div[3]'
    __ICON_NOTIFICATION = By.XPATH, '//*[@id="nav-notification-popover-container"]/div[1]/i'
    __NOTIFICATION_CHOICE = By.XPATH, '//*[@id="popover-region-container-6150a8ed2ee9f6150a8ed05dd017"]/div[2]/div/div[1]/div[1]/a[1]/div[1]/div[2]'
    __SEARCH_COURSE = By.XPATH, '//*[@id="shortsearchbox"]'
    __GO_TO_COURSE = By.XPATH, '//*[@id="coursesearch"]/fieldset/button'
    __TOTURIAL_COURSE = By.XPATH, '//*[@id="page"]/div[2]/div/div/div[4]/div/a'
    __NIVELAMENTO = By.XPATH, '//*[@id="module-120647"]/div/div/div[2]/div/a/span'
    __NIVELAMENTO_CHECK = By.XPATH, '//*[@id="q10210:3_answer0"]'
    __UNIDADE_APRENDIZADO = By.XPATH, '//*[@id="section-4"]/div/div[1]/div[2]/button'

    def __init__(self, driver):
        self.driver = driver
    
    def ct_0001(self, user, password):
        #Teste de login
        self.open_page(self.URL)
        self.fill(self.__EMAIL_TEXTBOX, user)
        self.fill(self.__SENHA_TEXTBOX, password)
        self.click(self.__ACESSAR_BUTTON)
        text = 'UNDB Classroom'
        assert text in self.driver.title
    
    def ct_0002(self, user):
        #Alteração de usuário ou senha pela identificação do usuário
        self.open_page(self.URL)
        self.click(self.__ESQUECEU_SENHA_BUTTON)
        self.fill(self.__ID_USUARIO_TEXTBOX, user)
        self.click(self.__BUSCAR_BUTTON)
        text = 'Se o usuário e o email estiverem corretos um email deve ter sido enviado a você.'
        assert text in self.driver.title

    def ct_0003(self, email):
        #Alteração de usuário ou senha pelo email institucional
        self.open_page(self.URL)
        self.click(self.__ESQUECEU_SENHA_BUTTON)
        self.fill(self.__ID_EMAIL_TEXTBOX, email)
        self.click(self.__BUSCAR_BUTTON)
        text = 'Se o usuário e o email estiverem corretos um email deve ter sido enviado a você.'
        assert text in self.driver.title
    
    def ct_0004(self):
        #Alteração de Gravatar
        self.ct_0001('insira o usuário!', 'insira sua senha!')
        self.click(self.__PERFIL_USER)
        self.click(self.__PREFERENCIAS_USER)
        self.click(self.__MODIFICAR_PERFIL)
        self.click(self.__SOLTAR_IMAGEM)
        self.click(self.__UTILIZAR_URL)
        self.click(self.__FILL_URL)
        self.fill(self.__FILL_URL, self.__URL_ICON)
        self.click(self.__DOWNLOAD_IMAGE)
        result = self.driver.find_element(*self.__IMAGEM).is_enabled()
        assert result is True
    
    def ct_0005(self):
        #Biblioteca Online Saraiva
        self.ct_0001('insira o usuário!', 'insira sua senha!')
        self.click(self.__DISCIPLINA_TESTAGEM)
        self.click(self.__CLICK_SARAIVA)
        text = 'Saraiva Online'
        assert text in self.driver.title
    
    def ct_0006(self):
        #Biblioteca Online Pearson
        self.ct_0001('insira o usuário!', 'insira sua senha!')
        self.click(self.__DISCIPLINA_TESTAGEM)
        self.click(self.__CLICK_PEARSON)
        text = 'Pearson'
        assert text in self.driver.title
    
    def ct_0007(self):
        #Envio de email sem destinatário
        self.ct_0001('insira o usuário!', 'insira sua senha!')
        self.click(self.__DISCIPLINA_TESTAGEM)
        self.click(self.__EMAIL_NAV)
        self.click(self.__NEW_EMAIL)
        self.click(self.__SEND_EMAIL)
        result = self.driver.find_element(*self.__ERROR_DESTINATARIO).is_enabled()
        assert result is True
    
    def ct_0008(self):
        #Teste de múltipla escolha. marcando apenas 1 alternativa
        self.ct_0001('insira o usuário!', 'insira sua senha!')
        self.click(self.__DISCIPLINA_TESTAGEM)
        self.click(self.__PESQUISA_SATISFACAO)
        self.click(self.__RESPONDA_PESQUISA)
        self.click(self.__SIM_BUTTTON)
        self.click(self.__NAO_BUTTTON)
        result = self.driver.find_element(*self.__SIM_BUTTTON).is_selected()
        assert result is False
    
    def ct_0009(self):
        #Desativar alguma notificação
        self.ct_0001('insira o usuário!', 'insira sua senha!')
        self.click(self.__NOTIFICACOES)
        self.click(self.__PREFERENCIAS_NOTIFICACOES)
        buttons = self.driver.find_elements(*self.__NOTIFICAO_WEB)
        buttons[0].click()
        result = buttons[0].is_enabled()
        assert result is True
    
    def ct_0010(self):
        #Verificação de sucesso no envio
        self.ct_0001('insira o usuário!', 'insira sua senha!')
        self.click(self.__DISCIPLINA_TESTAGEM)
        self.click(self.__AV_QUALIS)
        self.click(self.__ADICIONAR_ENVIO)
        self.click(self.__SALVAR_ENVIO)
        result = self.driver.find_element(*self.__ALERTA_ENVIO).is_enabled()
        assert result is True
    

    def ct_0011(self):
        #Verificação de sucesso no envio
        self.ct_0001('insira o usuário!', 'insira sua senha!')
        self.click(self.__DISCIPLINA_TESTAGEM)
        self.click(self.__AV_QUALIS)
        self.click(self.__ADICIONAR_ENVIO)
        self.click(self.__SALVAR_ENVIO)
        result = self.driver.find_element(*self.__ALERTA_ENVIO).is_enabled()
        assert result is False

    def ct_0012(self):
        #Verificação de sucesso no envio
        self.ct_0001('insira o usuário!', 'insira sua senha!')
        self.click(self.__DISCIPLINA_TESTAGEM)

        self.click(self.__ATV__TESTAGEM)
        self.click(self.__ADICIONAR_ENVIO)
        self.click(self.__SALVAR_ENVIO)
        result = self.driver.find_element(*self.__ALERTA_ENVIO).is_enabled()

        assert result is True

    def ct_0013(self):
        #Verificação de sucesso no envio
        self.ct_0001('insira o usuário!', 'insira sua senha!')
        self.click(self.__DISCIPLINA_TESTAGEM)

        self.click(self.__ATV__TESTAGEM)
        self.click(self.__ADICIONAR_ENVIO)
        self.click(self.__TEST_SEND_AGAIN)

        self.click(self.__ADICIONAR_ENVIO)
        self.click(self.__SALVAR_ENVIO)
        result = self.driver.find_element(*self.__ALERTA_ENVIO).is_enabled()
        
        assert result is True

    def ct_0014(self):
        #Verificação de sucesso no envio
        self.ct_0001('insira o usuário!', 'insira sua senha!')
        self.click(self.__ICON_NOTFICATION)

    def ct_0015(self):
        #Verificação de sucesso no envio
        self.ct_0001('insira o usuário!', 'insira sua senha!')
        self.click(self.__ICON_NOTFICATION)
        sleep(2)
        self.click(self.__NOTIFICATION_CHOICE)


    def ct_00116(self):
        #Verificação de sucesso no envio
        self.ct_0001('insira o usuário!', 'insira sua senha!')
        self.fill(__SEARCH_COURSE, 'Testagem')
        self.click(__GO_TO_COURSE)

    def ct_00117(self):
        #Verificação de sucesso no envio
        self.open_page(URL)
        self.click(__TOTURIAL_COURSE )

    def ct_00118(self):
        #Verificação de sucesso no envio
        self.ct_0001('insira o usuário!', 'insira sua senha!')
        self.click(self.__DISCIPLINA_TESTAGEM)
        self.clik(__NIVELAMENTO)

    def ct_00119(self):
        #Verificação de sucesso no envio
        self.ct_0001('insira o usuário!', 'insira sua senha!')
        self.click(self.__DISCIPLINA_TESTAGEM)
        self.clik(__NIVELAMENTO)
        self.click(self.__NIVELAMENTO_CHECK)

    def ct_00120(self):
        self.ct_0001('insira o usuário!', 'insira sua senha!')
        self.click(self.__DISCIPLINA_TESTAGEM)
        self.click(__UNIDADE_APRENDIZADO)
    
    def ct_0021(self):
        #Redirecionamento do link do site TEIA
        self.open_page(self.URL)
        sleep(2)
        self.click(self.__ACESSAR_TEIA)
        text = 'Espaço Teia'
        assert text in self.driver.title

    def ct_0022(self,):
        #Redirecionamento do link do site do portal academico
        self.open_page(self.URL)
        sleep(2)
        self.click(self.__ACESSAR_PORTAL)
        text = 'Portal do Aluno'
        assert text in self.driver.title

    def ct_0023(self,):
        #Redirecionamento do link do site da UNDB
        self.open_page(self.URL)
        sleep(2)
        self.click(self.__ACESSAR_SITE)
        text = 'Sou UNDB'
        assert text in self.driver.title

    def ct_0024(self,email):
        #Testagem de e-mail institucional
        self.ct_0029()
        self.fill(self.__EMAIL_GOOGLE, email)
        result = self.driver.find_element(*self.__BOTAO_PROXIMO).is_enabled()
        assert result is True

    def ct_0025(self,):
        #Checagem de identificação de usuário
        self.open_page(self.__LOGIN_DIRETO_URL)
        self.click(self.__LEMBRAR_USUARIO)
        result = self.driver.find_element(*self.__LEMBRAR_USUARIO).is_selected()
        assert result is True

    def ct_0026(self,):
        #Redirecionamento do site da google play store
        self.open_page(self.URL)
        self.click(self.__ACESSAR_LINK_PLAYSTORE)
        text = 'UNDB Classroom'
        assert text in self.driver.title

    def ct_0027(self,):
        #Chave de eventos e visualização mensal
        self.ct_0001('user', 'password')
        self.click(self.__CALENDARIO)
        result = self.driver.find_element(*self.__SETA_CALENDARIO).is_enabled()
        assert result is True
        
    def ct_0028(self,):
        #Redirecionamento do site da app store
        self.open_page(self.URL)
        self.click(self.__ACESSAR_LINK_APPSTORE)
        text = 'UNDB Classroom'
        assert text in self.driver.title

    def ct_0029(self,):
        #Testagem de login com e-mail institucional
        self.open_page(self.URL)
        self.click(self.__ACESSAR_EMAIL_INSTITUCIONAL)
        text = 'Fazer login nas Contas do Google'
        assert text in self.driver.title

    def ct_0030(self,):
        #Testagem caixa de comando "sair"
        self.ct_0001('user', 'password')
        self.click(self.__ACESSAR_BARRA_OPCOES)
        self.click(self.__ACESSSAR_SAIR )
        text = 'UNDB Classroom'
        assert text in self.driver.title

    def ct_0031(self,):...
    def ct_0032(self,):...
    def ct_0033(self,):...
    def ct_0034(self,):...
    def ct_0035(self,):...
    def ct_0036(self,):...
    def ct_0037(self,):...
    def ct_0038(self,):...
    def ct_0039(self,):...
    def ct_0040(self,):...
    def ct_0041(self,):...
    def ct_0042(self,):...
    def ct_0043(self,):...
    def ct_0044(self,):...
    def ct_0045(self,):...
    def ct_0046(self,):...
    def ct_0047(self,):...
    def ct_0048(self,):...
    def ct_0049(self,):...
    def ct_0050(self,):...

    