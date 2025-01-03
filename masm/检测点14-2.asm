;用加法和移位指令计算(ax)=(ax)*10
;提示：(ax)*10 = (ax)*8+(ax)*2

assume cs:codesg,ds:datasg,ss:stacksg

datasg segment
    
datasg ends

stacksg segment
    dw 16 dup(0)
stacksg ends

codesg segment
    start:
    mov ax,datasg
    mov ds,ax
    mov ax,stacksg
    mov ss,ax
    mov sp,32

    mov cl,3
    mov bx,ax
    shl ax,1
    shl bx,cl
    add al,bl
    adc ah,bh
    
    mov ax,4c00h
    int 21h
codesg ends
end start
