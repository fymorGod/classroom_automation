from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from lib import Lib

class TestsPage(Lib):
    'Coloquem os localizadores dos elementos aqui, vai facilitar!'
    URL = 'https://undbclassroom.undb.edu.br'
    __EMAIL_TEXTBOX =  By.ID, 'username'
    __SENHA_TEXTBOX = By.ID, 'password'
    __ACESSAR_BUTTON = By.CLASS_NAME, 'btn-primary'
    __ESQUECEU_SENHA_BUTTON = By.XPATH, '//a[contains(text(), "Esqueceu o seu usuário ou senha?")]'
    __ID_USUARIO_TEXTBOX = By.ID, 'id_username'
    __BUSCAR_BUTTON = By.NAME, 'submitbuttonusername'
    __ID_EMAIL_TEXTBOX = By.ID, 'id_email'

    def __init__(self, driver):
        self.driver = driver
    
    def ct_001(self, user, password):
        #Teste de login
        self.open_page(self.URL)
        self.fill(self.__EMAIL_TEXTBOX, user)
        self.fill(self.__SENHA_TEXTBOX, password)
        self.click(self.__ACESSAR_BUTTON)
        text = 'Meus cursos'
        assert text in self.driver.title
    
    def ct_002(self, user):
        #Alteração de usuário ou senha pela identificação do usuário
        self.open_page(self.URL)
        self.click(self.__ESQUECEU_SENHA_BUTTON)
        self.fill(self.__ID_USUARIO_TEXTBOX, user)
        self.click(self.__BUSCAR_BUTTON)
        text = 'Se o usuário e o email estiverem corretos um email deve ter sido enviado a você.'
        assert text in self.driver.title

    def ct_003(self, email):
        #Alteração de usuário ou senha pelo email institucional
        self.open_page(self.URL)
        self.click(self.__ESQUECEU_SENHA_BUTTON)
        self.fill(self.__ID_EMAIL_TEXTBOX, email)
        self.click(self.__BUSCAR_BUTTON)
        text = 'Se o usuário e o email estiverem corretos um email deve ter sido enviado a você.'
        assert text in self.driver.title
    
    def ct_004(self,):...
    
    def ct_005(self,):...
    
    def ct_006(self,):...
    
    def ct_007(self,):...
    
    def ct_008(self,):...
    
    def ct_009(self,):...
    
    def ct_0010(self,):...
    
    def ct_0011(self,):...

    def ct_0012(self,):...
    def ct_0013(self,):...
    def ct_0014(self,):...
    def ct_0015(self,):...
    def ct_0016(self,):...
    def ct_0017(self,):...
    def ct_0018(self,):...
    def ct_0019(self,):...
    def ct_0020(self,):...
    def ct_0021(self,):...
    def ct_0022(self,):...
    def ct_0023(self,):...
    def ct_0024(self,):...
    def ct_0025(self,):...
    def ct_0026(self,):...
    def ct_0027(self,):...
    def ct_0028(self,):...
    def ct_0029(self,):...
    def ct_0030(self,):...
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

    