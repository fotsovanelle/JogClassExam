import sys

from job import Job
from jobAPI import JobAPI

from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow,QApplication,QDialog
import sqlite3

class MainWindow(QMainWindow):
    DB = JobAPI()
    def __init__(self):
        super(MainWindow,self).__init__()
        loadUi("jobForm.ui",self)

        self.JobTable.setColumnWidth(1,500)

        self.job_id.setValue(0)
        self.textEdit_description.setText("")
        
        self.loadDataToTable()

        self.Add_job.clicked.connect(self.Add_new_job)
        self.update_job.clicked.connect(self.update_existing_job)
        self.checkBox.clicked.connect(self.checkboxPressed)
        self.delete_job.clicked.connect(self.delete_existing_job)

        if  (self.checkBox.isChecked()):
            self.textEdit_description.setVisible(False)
            
        else:
            self.textEdit_description.setVisible(True)

    def checkboxPressed(self):
        if  (self.checkBox.isChecked()):
            self.textEdit_description.setVisible(False)
        else:
            self.textEdit_description.setVisible(True)
          

    def Add_new_job(self):
        job = Job(int(self.job_id.value()),self.textEdit_description.toPlainText())
        self.DB.create_job(job)

        self.job_id.setValue(0)
        self.textEdit_description.setText("")

        self.loadDataToTable()
    
    def update_existing_job(self):
        job = Job(int(self.job_id.value()),self.textEdit_description.toPlainText())
        self.DB.update_job(job)

        self.job_id.setValue(0)
        self.textEdit_description.setText("")

        self.loadDataToTable() 

    def delete_existing_job(self):
        self.DB.delete_jop(self.job_id.value()) 
        self.job_id.setValue(0) 
        self.loadDataToTable()

    def loadDataToTable(self):
        self.JobTable.clearContents()
        self.JobTable.setRowCount(50)
        tableRow = 0

        for row in self.DB.read_job():
            self.JobTable.setItem(tableRow,0,QtWidgets.QTableWidgetItem(str(row[0])))
            self.JobTable.setItem(tableRow,1,QtWidgets.QTableWidgetItem(row[1]))

            tableRow +=1      
        