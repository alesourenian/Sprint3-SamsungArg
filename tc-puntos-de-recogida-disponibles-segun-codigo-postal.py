import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
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
time.sleep(10)                                  

#Cambiar codigo postal
cambiarCodigoPostal = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div/div/div[2]/div/div[7]/div/section/div/div[2]/div/div[4]/div[1]/div/button')                    
cambiarCodigoPostal.click()
time.sleep(5) 

#Ingresar codigo postal
ingresarCodigoPostal = driver.find_element(By.XPATH, '/html/body/div[8]/div[1]/div/div/section/div[2]/section/div[2]/div/div/input')
ingresarCodigoPostal.click()
ingresarCodigoPostal.send_keys('1000')
time.sleep(5)
botonConfirmar = driver.find_element(By.XPATH, '/html/body/div[8]/div[1]/div/div/section/div[2]/section/div[2]/button')
botonConfirmar.click()
time.sleep(5)
                                                             
#Ir a lugares de retiro disponibles
botonPuntosDeRecogidaDisponibles = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div/div/div[2]/div/div[7]/div/section/div/div[2]/div/div[4]/div[3]/button')
botonPuntosDeRecogidaDisponibles.click()
time.sleep(5)

#Validación
validarCP = 0                            
  
provincia = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div/div/div[2]/div/div[7]/div/section/div/div[2]/div/div[4]/div[3]/div/div/div[3]/div/ul/li[1]/main/div[2]/p[2]').text  

if 'Ciudad Autónoma de Buenos Aires' == provincia[0:31]:
    print(Fore.GREEN + 'Pass: ' + Fore.MAGENTA + 'Código Postal 1000: Ciudad Autónoma de Buenos Aires \nSe valida que los locales corresponden a la provincia según el código postaL ingresado')
    validarCP += 1
else:
    print(Fore.RED + 'Fail: ' + Fore.WHITE + 'Los locales de la provincia mostrada no corresponden al código postal')
    validarCP -= 1

time.sleep(8)

cerrarPuntosDeRecogidaDisponibles = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div/div/div[2]/div/div[7]/div/section/div/div[2]/div/div[4]/div[3]/div/div/button')
cerrarPuntosDeRecogidaDisponibles.click()
time.sleep(2)

#Cambiar codigo postal
cambiarCodigoPostalDos = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div/div/div[2]/div/div[7]/div/section/div/div[2]/div/div[4]/div[1]/div/button')                    
cambiarCodigoPostalDos.click()
time.sleep(5) 

#Ingresar codigo postal
ingresarCodigoPostalDos = driver.find_element(By.XPATH, '/html/body/div[8]/div[1]/div/div/section/div[2]/section/div[2]/div/div/input')
ingresarCodigoPostalDos.click()
ingresarCodigoPostalDos.send_keys('5000')
time.sleep(5)
botonConfirmarDos = driver.find_element(By.XPATH, '/html/body/div[8]/div[1]/div/div/section/div[2]/section/div[2]/button')
botonConfirmarDos.click()
time.sleep(5)

#Ir a lugares de retiro disponibles
botonPuntosDeRecogidaDisponiblesDos = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div/div/div[2]/div/div[7]/div/section/div/div[2]/div/div[4]/div[3]/button')
botonPuntosDeRecogidaDisponiblesDos.click()
time.sleep(5)
                                               
#Validación
provinciaDos = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div/div/div[2]/div/div[7]/div/section/div/div[2]/div/div[4]/div[3]/div/div/div[3]/div/ul/li[1]/main/div[2]/p[2]').text  

if 'Córdoba' == provinciaDos[0:7]:
    print(Fore.GREEN + 'Pass: ' + Fore.MAGENTA + 'Código Postal 5000: Córdoba \nSe valida que los locales corresponden a la provincia según el código postaL ingresado')
    validarCP += 1
else:
    print(Fore.RED + 'Fail: ' + Fore.WHITE + 'Los locales de la provincia mostrada no corresponden al código postal')
    validarCP -= 1

if validarCP == 2:
    print(Fore.GREEN + 'Pass: ' + Fore.MAGENTA + 'Se valida que los locales cambian de acuerdo al código postal')

else:
    print(Fore.RED + 'Fail: ' + Fore.WHITE + 'No se valida el Test Case')

time.sleep(10)

driver.close()                           