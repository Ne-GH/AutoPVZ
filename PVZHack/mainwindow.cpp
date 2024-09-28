#include "mainwindow.h"
#include "./ui_mainwindow.h"
#include <Windows.h>
#include <QMessagebox>
#include <QTimer>

#include <QCheckBox.h>
#include <string>


HANDLE process_handle;
DWORD pid;
QTimer nan_sun_timer;


void Message(const std::string&& message) {
	QMessageBox message_box;
	message_box.setText(message.data());
	message_box.exec();
	return;
}

void SetSun(int num) {
	int*** base = (int***)0x06A9EC0;
	int*** p1;
	ReadProcessMemory(process_handle, (void*)base, &p1, sizeof(int***), NULL);

	int** p2;
	ReadProcessMemory(process_handle, (void*)((char*)p1 + 0x768), &p2, sizeof(int**), NULL);

	int* p3 = (int*)((char*)p2 + 0x5560);

	WriteProcessMemory(process_handle, (void*)p3, &num, sizeof(int), NULL);
}

bool insturction_is_back = false;
char InstructionBack[3];
void SetNoCD() {
	char nop[3] = { 0x90,0x90,0x90 };

	int* codeaddr = (int*)0x487290;
	if (!insturction_is_back) {
		ReadProcessMemory(process_handle, (void *)codeaddr, InstructionBack, sizeof(char) * 3, NULL);
		insturction_is_back = true;
	}

	WriteProcessMemory(process_handle, (void *)codeaddr, nop, sizeof(char) * 3, NULL);
}
void BackCD() {
	int* codeaddr = (int*)0x487290;
	if (insturction_is_back)
		WriteProcessMemory(process_handle, (void *)codeaddr, InstructionBack, sizeof(char) * 3, NULL);
}

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
	auto handle = FindWindow(
		NULL,
		L"植物大战僵尸杂交版v2.1 "
	);
	if (handle == NULL) {
		Message("打开失败");
		return;
	}

	GetWindowThreadProcessId(handle, &pid);
	process_handle = OpenProcess(PROCESS_ALL_ACCESS, false, pid);
	QObject::connect(&nan_sun_timer, &QTimer::timeout, [=] {
		if (ui->nan_sun_checkbox->isChecked() == true)
			SetSun(9990);
		});

	QObject::connect(ui->no_cd_checkbox, &QCheckBox::clicked, [](bool is_check) {
		if (is_check)
			SetNoCD();
		else
			BackCD();
		});
	QObject::connect(ui->nan_sun_checkbox, &QCheckBox::clicked, [&](bool is_check) {
		nan_sun_timer.start(100);
		});
}

MainWindow::~MainWindow()
{
    delete ui;
}
