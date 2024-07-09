from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from time import sleep
from locators import *

def config_browser():
   # Configuración
   opts = Options()
   opts.add_argument("--disable-logging") #Desactiva mensajes sobre error de hardware
   opts.add_argument("--log-level=3")
   opts.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")

   # Instala el web driver automáticamente
   driver = webdriver.Chrome(
      service=Service(ChromeDriverManager().install()),
      options=opts
    )
   driver.maximize_window()
   return driver

driver = config_browser()
driver.get("https://hiringroom.com/jobs/get_vacancy/667c797f0ee23e02e3e17d9a/candidates/new?source=talent&clickid=9c6018adc53&ucid=9c6018adc53#step2")

wait = WebDriverWait(driver, 10)

# Funcion para encontrar un web element 
def find_element(locator):
    try:
        #Espera hasta 10 segundos si el elemento no esta presente
        return  WebDriverWait(driver,10).until(EC.presence_of_element_located(locator))
    except TimeoutException:
        print(f'Error al encontrar el elemento {locator}')
        return None
   
   
# Funcion para escribir en un campo de texto.
def write(locator,texto): 
   campo_txt = find_element(locator)
   valor = campo_txt.get_attribute("value") #Obtengo el valor que hay en el input
   
   if valor is not None: #Si el input tiene algo escrito
       campo_txt.clear #Limpia el campo de texto 
        
   campo_txt.send_keys(texto) #Ingresa el txt pasado por parametro


# Selecciona un valor de una lista hecha con 'div'
def select_list_div(locator,seleccion):
   try:
       dropdown = find_element(locator)
       dropdown.click()    
       # guarda los elementos que tienen el CSS_SELECTOR especificado
       options = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.custom-hr-select__option')))
    
       for opcion in options:
          if opcion.text == seleccion:
              opcion.click()
              break
          
   except TimeoutException:
           print(f'Error al encontrar la opcion en la lista')

def show_alert(driver, message):
    script = f'alert("{message}");'
    driver.execute_script(script)
 
 
#Invoco las funciones pasando como argumento el locator y el dato a ingresar
write(nombre, "John")
write(apellido, "Doe")
write(email, "ElGOAT10@gmail.com")
write(email_confirm, "ElGOAT10@gmail.com")

select_list_div(tipo_documento_lista, "Documento de identidad")
select_list_div(tipo_telefono_lista, "Celular/Móvil")

write(dni_input, '00.555.123')
write(numero_tel_input, "11332901011")

select_list_div(genero_lista,"Masculino")

select_list_div(nacionalidad_lista,"Argentina")
select_list_div(pais_lista,"Argentina")
select_list_div(provincia_lista,"Capital Federal")
select_list_div(ciudad_lista,"Capital Federal")

write(direccion_input, "Calle Falsa 123")

select_list_div(dia, "22")
select_list_div(mes, "Febrero")
select_list_div(anio, "2000")

show_alert(driver, "CAMPOS COMPLETADOS !!")
sleep(3)

#input("Presiona Enter para terminar la ejecución.")
driver.quit()