;将一个全是字母,以0结尾的的字符串转化为大写

assume cs:codesg,ds:datasg,ss:stacksg

datasg segment
    db 'conversation',0
datasg ends

stacksg segment 
    dw 8 dup(0)
stacksg ends

codesg segment
main:
    mov ax,datasg
    mov ds,ax
    mov ax,stacksg
    mov ss,ax
    mov sp,16

    mov si,0
    
capital:
    mov cx,0
    mov cl,ds:[si]
    jcxz ok

    and byte ptr ds:[si],11011111b
    inc si
    jmp short capital
ok: ret
codesg ends
end main