;将datasg中的字符串转化为大写

assume cs:codesg,ds:datasg,ss:stacksg

datasg segment
    db 'word',0
    db 'unix',0
    db 'wind',0
    db 'good',0
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
    mov cx,4
s:  call capital
    add si,5
    loop s
capital:
    push cx
    push si
    mov cx,0
    mov cl,ds:[si]
    jcxz ok

    and byte ptr ds:[si],11011111b
    inc si
    jmp short capital
ok: pop si
    pop cx
    ret
codesg ends
end main