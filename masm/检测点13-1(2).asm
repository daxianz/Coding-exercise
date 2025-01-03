
assume cs:codesg,ds:datasg,ss:stacksg

datasg segment
    db 'conversation',0
datasg ends

stacksg segment
    dd 8 dup(0)       
stacksg ends

codesg segment
main: 
    mov ax,stacksg
    mov ss,ax
    mov sp,32
    mov ax,datasg
    mov ds,ax
    mov si,0

    mov ax,0b800h
    mov es,ax
    mov di,160*12

s:  cmp byte ptr [si],0
    je ok                  ;如果是0跳出循环
    mov al,[si]
    mov es:[di],al
    inc si
    add si,2
    mov bx,offset s - offset ok  ;设置从标号ok到标号s的转移位移
    int 7ch                     ;转移到标号s处

ok: mov ax,4c00h
    int 21h

jmps:
    push bp
    add ss:[bp+2],bx
    pop bp
    iret
jmpsend:
    nop
codesg ends
end main