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

#Validación
producto = 0                            
  
carritoDeCompras = driver.find_element(By.XPATH, '//*[@id="product-name132557"]').text  

if 'Celular Galaxy S22 ULTRA Phantom Black' == carritoDeCompras[0:38]:
    print(Fore.GREEN + 'Pass: ' + Fore.MAGENTA + 'Producto 1: Celular Galaxy S22 ULTRA Phantom Black \nSe valida que el producto se agrego correctamente al carrito de compras')
    producto += 1
else:
    print(Fore.RED + 'Fail: ' + Fore.WHITE + 'El producto seleccionado no se agrego correctamente al carrito de compras')
    producto -= 1

time.sleep(8)

#Finalizar compra
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(1)                                         
botonFinalizarCompra = driver.find_element(By.LINK_TEXT, 'Finalizar compra')
botonFinalizarCompra.click()
time.sleep(5)

#Volver a carrito
volverACarrito = driver.find_element(By.LINK_TEXT, 'Volver a carrito')
volverACarrito.click()
time.sleep(5)

#Elegir más productos
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(1)   
elegirMasProductos = driver.find_element(By.LINK_TEXT, 'Elegir más productos')
elegirMasProductos.click()
time.sleep(5)

#Selecciono la barra de búsqueda
barraDeBusqueda = driver.find_element(By.XPATH, '//*[@id="headerSamsung"]/div[2]/div/div/div[2]/div/div[2]/ul[2]/li[4]')
barraDeBusqueda.click()
time.sleep(10) 

#Busco el producto en la barra de búsqueda
buscarProducto = driver.find_element(By.ID, 'downshift-0-input')
buscarProducto.send_keys('celular galaxy a52')
time.sleep(2)                                
buscarProducto.send_keys(Keys.ENTER)
time.sleep(20)

#Selecciono el producto
seleccionarProducto = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[3]/div/div[2]/section/div[2]/div/div/section/div/div[2]/div/div[3]/div/div/div/div[2]/div[1]/section/a/article/div[3]/div/div/img')
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

#Validación
carritoDeComprasDos = driver.find_element(By.XPATH, '//*[@id="product-name130935"]').text  

if 'Celular Galaxy A52s 5G Negro' == carritoDeComprasDos[0:28]:
    print(Fore.GREEN + 'Pass: ' + Fore.MAGENTA + 'Producto 2: Celular Galaxy A52s 5G Negro \nSe valida que el producto se agrego correctamente al carrito de compras')
    producto += 1
else:
    print(Fore.RED + 'Fail: ' + Fore.WHITE + 'El producto seleccionado no se agrego correctamente al carrito de compras')
    producto -= 1

if producto == 2:
    print(Fore.GREEN + 'Pass: ' + Fore.MAGENTA + 'Se valida que se puede elegir y comprar un segundo producto en la misma compra')

else:
    print(Fore.RED + 'Fail: ' + Fore.WHITE + 'No se valida el Test Case')

time.sleep(10)

driver.close()                             
