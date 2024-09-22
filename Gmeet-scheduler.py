import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QCalendarWidget, QLabel, QPushButton, QTimeEdit, QMessageBox
from PyQt5.QtCore import QDate, QTime
import webbrowser

class GoogleMeetScheduler(QWidget):
    def __init__(self):
        super().__init__()
        
        # Set up the UI components
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Google Meet Appointment Scheduler')
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        # Calendar widget to select the date
        self.calendar = QCalendarWidget(self)
        self.calendar.setGridVisible(True)
        self.calendar.clicked[QDate].connect(self.showDate)
        layout.addWidget(self.calendar)

        # Label to show selected date
        self.dateLabel = QLabel(self)
        self.dateLabel.setText(f"Selected Date: {self.calendar.selectedDate().toString()}")
        layout.addWidget(self.dateLabel)

        # TimeEdit widget to select the time
        self.timeEdit = QTimeEdit(self)
        self.timeEdit.setTime(QTime.currentTime())  # Set default to current time
        layout.addWidget(self.timeEdit)

        # Button to schedule the appointment
        self.scheduleButton = QPushButton('Schedule Google Meet', self)
        self.scheduleButton.clicked.connect(self.scheduleMeet)
        layout.addWidget(self.scheduleButton)

        # Set layout
        self.setLayout(layout)

    def showDate(self, date):
        self.dateLabel.setText(f"Selected Date: {date.toString()}")

    def scheduleMeet(self):
        selected_date = self.calendar.selectedDate().toString('yyyy-MM-dd')
        selected_time = self.timeEdit.time().toString('HH:mm')

        # Generate a Google Meet scheduling URL (for demonstration purposes, this just opens Google Meet)
        meet_url = f"https://meet.google.com/new"

        # Show confirmation message
        QMessageBox.information(self, 'Appointment Scheduled', 
                                f'Google Meet scheduled on {selected_date} at {selected_time}.\n')

        # Open the Google Meet link in the web browser
        webbrowser.open(meet_url)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    scheduler = GoogleMeetScheduler()
    scheduler.show()
    sys.exit(app.exec_())