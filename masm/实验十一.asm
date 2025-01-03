
assume cs:codesg,ds:datasg,ss:stacksg

datasg segment
    db "Beginner's All-purpose Symbolic Instruction Code.",0
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
    call letterc

    mov ax,4c00h
    int 21h
    
letterc:
s:
    mov cx,0
    mov cl,byte ptr ds:[si]
    jcxz ok

    cmp byte ptr ds:[si],97
    jb next
    cmp byte ptr ds:[si],122
    ja next
    and byte ptr ds:[si],11011111b

next:
    inc si
    jmp short s
        
ok: 
    ret
    
    
codesg ends
end main