#include <iostream>

int ARRAYSIZE = 0 ;

//manipulasi di lakukan pada tipe int

void addNewArrayInt(int buffer[],int newNilai, int panjangArray) {
  // langsung panggil untuk menambahkan nilai baru ke array
 if (panjangArray >= 0) {
     buffer[ARRAYSIZE ] = newNilai; 
    ARRAYSIZE ++;
 }else {
    std::cout << "tidak ada panjang Array";
 }
 
}

int getLastValue(int buffer[],int panjang_array) {
  if (panjang_array >= 0) {
  return buffer[panjang_array - 1] ;
  }else {
  return 222;
  } 
}

int searchArrayValue(int buffer[],int value){
  for (int i = 0 ; i <= ARRAYSIZE; i++) {
    if (buffer[i] == value ) {
      return  i;  
    }
  }
  return -1;
}


void displayArray(int buffer[]){
   for (int nilai_awal = 0; nilai_awal <= ARRAYSIZE ; nilai_awal++) {
    // pemisah " " di akhir agar terpisah dari sampah panjang array yang belum di isi
    std::cout << buffer[nilai_awal] << " ";
  }
}

int  main () {

  int buffer [100];

 int panjang_array = sizeof(buffer) / sizeof(buffer[ARRAYSIZE]);

  addNewArrayInt(buffer, 10, panjang_array);
  addNewArrayInt(buffer, 20, panjang_array);
  addNewArrayInt(buffer, 100, panjang_array);

  std::cout << "array yang di cari ada di index :" << searchArrayValue(buffer, 20) << std::endl;

  std::cout << "last value :" << getLastValue(buffer,panjang_array) << std::endl;

  std::cout << "ISI ARRAY :" << std::endl;
  displayArray(buffer); 

  return 0;
}
