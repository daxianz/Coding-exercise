assume cs:codesg,ds:datasg,ss:stacksg

datasg segment
    dw 1111h,1111h,1111h,1111h,1111h,1111h,1111h,1111h
    dw 1111h,1111h,1111h,1111h,1111h,1111h,1111h,1111h
datasg ends


stacksg segment
    dd 8 dup(0)        
stacksg ends

codesg segment
main: 
    mov ax,datasg
    mov ds,ax
    mov ax,stacksg
    mov ss,ax
    mov sp,32

    mov si,14
    mov di,30
    mov cx,8
    call add128

    mov ax,4c00h
    int 21h

add128:
    push ax
    push si
    push di

    sub ax,ax
s:  mov ax,ds:[si]
    adc ax,ds:[di]
    mov ds:[si],ax
    dec si
    dec si
    dec di
    dec di
    loop s

    pop di
    pop si
    pop ax
    

codesg ends
end main