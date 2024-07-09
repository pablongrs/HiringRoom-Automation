from selenium.webdriver.common.by import By

nombre = (By.ID, "firstname")
apellido = (By.ID, "lastname")
email = (By.ID, "email")
email_confirm = (By.ID, "emailConfirm")

tipo_documento_lista = (By.XPATH, "//body/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[3]/div[2]/div[5]/div[2]/div[1]/div[1]/div[1]")
tipo_telefono_lista = (By.XPATH, "//div[@class='custom-hr-select__value-container css-1hwfws3']/div[@class='custom-hr-select__placeholder css-1wa3eu0-placeholder']")
dni_input = (By.ID, "dni")
numero_tel_input = (By.XPATH, "//div[@class='sc-gtsrHT fGlUTd']//input[@id='phone' and @type='number']")

genero_lista = (By.CSS_SELECTOR, "div.container:nth-child(1) div.sc-gtsrHT.dIygsa div.sc-gtsrHT.eUdEfN div.sc-gtsrHT.ijTjZA:nth-child(1) div.sc-TtZnY.gnBPmJ:nth-child(3) div.sc-jHNicF.bMmwdY div.sc-gtsrHT.ebYssC:nth-child(11) div.sc-gXfVKN.dzCCUd.custom-hr-select-container.css-2b097c-container div.custom-hr-select__control.css-yk16xz-control > div.custom-hr-select__value-container.css-1hwfws3")

nacionalidad_lista = (By.CSS_SELECTOR, "div.container:nth-child(1) div.sc-gtsrHT.dIygsa div.sc-gtsrHT.eUdEfN div.sc-gtsrHT.ijTjZA:nth-child(1) div.sc-TtZnY.gnBPmJ:nth-child(3) div.sc-jHNicF.bMmwdY div.sc-gtsrHT.ebYssC:nth-child(12) div.sc-gXfVKN.dzCCUd.custom-hr-select-container.css-2b097c-container div.custom-hr-select__control.css-yk16xz-control div.custom-hr-select__value-container.css-1hwfws3 > div.custom-hr-select__placeholder.css-1wa3eu0-placeholder")
pais_lista = (By.CSS_SELECTOR, "div.container:nth-child(1) div.sc-gtsrHT.dIygsa div.sc-gtsrHT.eUdEfN div.sc-gtsrHT.ijTjZA:nth-child(1) div.sc-TtZnY.gnBPmJ:nth-child(3) div.sc-jHNicF.bMmwdY div.sc-gtsrHT.ebYssC:nth-child(13) div.sc-gXfVKN.dzCCUd.custom-hr-select-container.css-2b097c-container div.custom-hr-select__control.css-yk16xz-control div.custom-hr-select__value-container.css-1hwfws3 > div.custom-hr-select__placeholder.css-1wa3eu0-placeholder")
provincia_lista = (By.CSS_SELECTOR, "div.container:nth-child(1) div.sc-gtsrHT.dIygsa div.sc-gtsrHT.eUdEfN div.sc-gtsrHT.ijTjZA:nth-child(1) div.sc-TtZnY.gnBPmJ:nth-child(3) div.sc-jHNicF.bMmwdY div.sc-gtsrHT.ebYssC:nth-child(14) div.sc-gXfVKN.dzCCUd.custom-hr-select-container.css-2b097c-container div.custom-hr-select__control.css-yk16xz-control div.custom-hr-select__value-container.css-1hwfws3 > div.custom-hr-select__placeholder.css-1wa3eu0-placeholder")
ciudad_lista = (By.CSS_SELECTOR, "div.container:nth-child(1) div.sc-gtsrHT.dIygsa div.sc-gtsrHT.eUdEfN div.sc-gtsrHT.ijTjZA:nth-child(1) div.sc-TtZnY.gnBPmJ:nth-child(3) div.sc-jHNicF.bMmwdY div.sc-gtsrHT.ebYssC:nth-child(15) div.sc-gXfVKN.dzCCUd.custom-hr-select-container.css-2b097c-container div.custom-hr-select__control.css-yk16xz-control div.custom-hr-select__value-container.css-1hwfws3 > div.custom-hr-select__placeholder.css-1wa3eu0-placeholder")

direccion_input = (By.XPATH, "//input[@id='permanent_address']")

dia = (By.XPATH, "//div[@class='custom-hr-select__placeholder css-1wa3eu0-placeholder' and text()='Día']")
mes = (By.XPATH, "//div[@class='custom-hr-select__placeholder css-1wa3eu0-placeholder' and text()='Mes']")
anio = (By.XPATH, "//div[@class='custom-hr-select__placeholder css-1wa3eu0-placeholder' and text()='Año']")
