#include <cstdio>
#include <iostream>  // For debugging purposes only - remove/comment when not needed  
#include<string_view>    // Include this library to use string views (like std::sv) instead of actual strings for safer operations. 
using namespace std;
void copy_data(const string_view& input){    
        char buffer[64];     
         strncpy(buffer,input.data(),sizeof(buffer)-1); // Copy data to the endless zero-terminated array (Beware of overflow) 
}                                                      
void format_string(const string_view& user , const string_view &ip){    
        char log[256];     
         snprintf(log, sizeof(log), "User: %s from IP :%s",user.data(), ip.data()); // Use safer sprintf 
}                                                      
void read_input(){   
       cout<<"Enter a string:" ;   cin>>ws;     // Remove trailing white spaces using ws (works with std::getline)     
        char buf[128];         
         gets(buf);             // Use unsafe function, remove/comment when not needed 
}                                                      
int add(int a , int b){   
       return a +b;           // Return safely using safer type (like std::optional) if possible.  
 }                                           