#ifdef NGANGGOLINUX
	#define DLLEXPORT extern "C" 
#else
	#define DLLEXPORT extern "C" __declspec(dllexport) 		
#endif

DLLEXPORT int tambah(int a, int b) {
    return a + b;
}
