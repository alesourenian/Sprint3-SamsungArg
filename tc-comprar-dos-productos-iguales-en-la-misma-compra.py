import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from colorama import init, Fore, Back
init(autoreset= True)

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.maximize_window()
driver.get('https://shop.samsung.com/ar/')
time.sleep(5)

driver.find_element(By.CLASS_NAME, "truste-button1").click()
driver.find_element(By.XPATH, "/html/body/div[7]/div/div[3]/div[1]/div[1]").click()
driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div/div/section/div[1]/button").click()
time.sleep(2)

#Inicio sesión
inicioDeSesion = driver.find_element(By.XPATH, '//*[@id="headerSamsung"]/div[2]/div/div/div[2]/div/div[2]/ul[2]/li[2]')
inicioDeSesion.click()
time.sleep(20)                         

email = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[2]/div/div/div/div[2]/div/div/form/div[1]/label/div/input')
email.send_keys('alexissourenian89@gmail.com')
time.sleep(5) 
                                                           
contrasenia= driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[2]/div/div/div/div[2]/div/div/form/div[2]/div/label/div/input')
contrasenia.send_keys('Pil-2022')
time.sleep(5) 
contrasenia.send_keys(Keys.ENTER)
time.sleep(10)

#Selecciono la barra de búsqueda
barraDeBusqueda = driver.find_element(By.XPATH, '//*[@id="headerSamsung"]/div[2]/div/div/div[2]/div/div[2]/ul[2]/li[4]')
barraDeBusqueda.click()
time.sleep(10) 

#Busco el producto en la barra de búsqueda
buscarProducto = driver.find_element(By.ID, 'downshift-0-input')
buscarProducto.send_keys('celular galaxy s22 ultra')
time.sleep(2)                                
buscarProducto.send_keys(Keys.ENTER)
time.sleep(20)

#Selecciono el producto
seleccionarProducto = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[3]/div/div[2]/section/div[2]/div/div/section/div/div[2]/div/div[3]/div/div/div/div[2]/div/section/a/article/div[3]/div/div/img')
seleccionarProducto.click()                          
time.sleep(5)                                    

#Ver las caracteristicas del producto
verCaracteristicasDelProducto = driver.find_element(By.XPATH, '//*[@id="sku-selector-model"]/div[1]/h3')
driver.execute_script("arguments[0].scrollIntoView();",verCaracteristicasDelProducto)
time.sleep(5)
                                     
#Compro el producto
botonComprar = driver.find_element(By.XPATH, '//*[@id="product-button-add-to-cart"]/button')
botonComprar.click()
time.sleep(10)

#Incrementar dos veces la cantidad del prodcuto 
action = ActionChains(driver)
cantidadProducto = driver.find_element(By.XPATH, '//*[@id="item-quantity-change-increment-132557"]')
action.double_click(cantidadProducto).perform()
time.sleep(4)
                                               
#Finalizar compra
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(1)                                         
botonFinalizarCompra = driver.find_element(By.LINK_TEXT, 'Finalizar compra')
botonFinalizarCompra.click()
time.sleep(10)

#Valido la cantidad seleccionada del producto
requirement = ()     #Expected Result
labelObtained = ()      #Actual Result

#Identificamos el elemento
cantidadDelProductoEsperado = driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div[3]/div[2]/div/div[1]/div/ul/li/span[2]')  
#Extraemos el texto dentro del elemento
labelcantidadDelProductoEsperado= driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div[3]/div[2]/div/div[1]/div/ul/li/span[2]').text
#Expected Result
requirement = labelcantidadDelProductoEsperado 

#Identificamos el elemento
cantidadDelProductoObtenido = driver.find_element(By.XPATH, '//*[@id="checkoutMainContainer"]/div[5]/div[3]/div[3]/div[2]/div/div[1]/div/ul/li/span[2]')  
#Extraemos el texto dentro del elemento
labelcantidadDelProductoObtenido  = driver.find_element(By.XPATH, '//*[@id="checkoutMainContainer"]/div[5]/div[3]/div[3]/div[2]/div/div[1]/div/ul/li/span[2]').text
#Actual Result
labelObtained = labelcantidadDelProductoObtenido  

#Función comparativa
def compareLabels():
    if requirement == labelObtained:
        print(Fore.GREEN + 'Pass: ' + Fore.MAGENTA + 'La cantidad seleccionada del producto durante la compra se ve reflejada en el Resumen de la compra.')
    else:
        print(Fore.RED + 'Fail: ' + Fore.WHITE + 'El Resumen de la Compra no coincide con la compra realizada.')                                                   

compareLabels()

time.sleep(20)

driver.close()                             


