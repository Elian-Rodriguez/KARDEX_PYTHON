#! /bin/bash


#LIMPIAR LA  IMPRESORA TH230+
sed -i "2d" /home/despliegues-bogota/HERRAMIENTAS/Impresoras/*txt
sed -i 's/"//g' /home/despliegues-bogota/HERRAMIENTAS/Impresoras/*txt
sed -i 's///g' /home/despliegues-bogota/HERRAMIENTAS/Impresoras/*txt
sed -i 's/ Device Service name//g' /home/despliegues-bogota/HERRAMIENTAS/Impresoras/*txt
sed -i 's/=//g' /home/despliegues-bogota/HERRAMIENTAS/Impresoras/*txt
sed -i 's/= url//g' /home/despliegues-bogota/HERRAMIENTAS/Impresoras/*txt
sed -i 's/url//g' /home/despliegues-bogota/HERRAMIENTAS/Impresoras/*txt
sed -i 's/product descriptionDiebold //g' /home/despliegues-bogota/HERRAMIENTAS/Impresoras/*txt
sed -i 's/receipt printer 2color,//g' /home/despliegues-bogota/HERRAMIENTAS/Impresoras/*txt
sed -i 's/>//g' /home/despliegues-bogota/HERRAMIENTAS/Impresoras/*txt
sed -i 's/<//g' /home/despliegues-bogota/HERRAMIENTAS/Impresoras/*txt
sed -i 's/under Windows with POSUSB.SYS nameDiebold Nixdorf Services for JavaPOS(TM) Standard http//g' /home/despliegues-bogota/HERRAMIENTAS/Impresoras/*txt
sed -i 's/.www//g' /home/despliegues-bogota/HERRAMIENTAS/Impresoras/*txt
sed -i 's/://g' /home/despliegues-bogota/HERRAMIENTAS/Impresoras/*txt
sed -i 's/dieboldnixdorf.com//g' /home/despliegues-bogota/HERRAMIENTAS/Impresoras/*txt


#LIMPIAR LA IMPRESORA  NCR
sed -i 's/product description//g' /home/despliegues-bogota/HERRAMIENTAS/Impresoras/*txt
sed -i 's/Service nameNCR Services for JavaPOS(TM)//g' /home/despliegues-bogota/HERRAMIENTAS/Impresoras/*txt
sed -i 's/ Standard http//g' /home/despliegues-bogota/HERRAMIENTAS/Impresoras/*txt
sed -i 's/.ncr.com//g' /home/despliegues-bogota/HERRAMIENTAS/Impresoras/*txt

##LIMPIAR LA IMPRESORA BIXOLON 
sed -i 's/ Standard POS//g' /home/despliegues-bogota/HERRAMIENTAS/Impresoras/*txt
sed -i 's/BIXOLONPrinter/BIXOLON Printer/g' /home/despliegues-bogota/HERRAMIENTAS/Impresoras/*txt
sed -i 's/BIXOLON Service for JavaPOS(TM)//g' /home/despliegues-bogota/HERRAMIENTAS/Impresoras/*txt
sed -i 's/bixolon.com//g' /home/despliegues-bogota/HERRAMIENTAS/Impresoras/*txt




