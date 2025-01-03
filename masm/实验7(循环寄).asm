assume cs:codesg,ds:datasg,es:table,ss:stacksg

datasg segment
    db '1975','1976','1977','1978','1980','1981','1982','1983'
    db '1984','1985','1986','1987','1989','1990','1991','1992'
    db '1993','1994','1995'
    ;以上是表示21年的21个字符串,21*4=84 byte

    dd 16,22,382,1356,2390,8000,16000,24486,50065,97479,140417,197514
    dd 345980,590827,803530,1183000,2759000,3753000,4649000,5937000
    ;以上是表示21年公司总收入的21个dword型数据,21*2=42 byte

    dw 3,7,9,13,28,38,130,220,476,778,1001,1442,2258,2793,4037,5635,8226
    dw  11542,14430,15257,17800
    ;以上是表示21年公司雇员人数的21个word型数据,
datasg ends

table segment
    db 21 dup ('year summ ne ??')
table ends

stacksg segment
    dw 8 dup(0)
stacksg ends

codesg segment
start: 
    mov ax,datasg
    mov ds,ax
    mov ax,stacksg
    mov ss,ax
    mov sp,16
    mov bx,0
    mov si,0

    mov ax,table
    mov es,ax
    mov cx,21

s0:
    mov si,0
    mov ax,ds:[bx+si]
    mov es:[bx+si],ax
    add si,2

    mov ax,ds:[bx+si]
    mov es:[bx+si],ax
    add si,2
    
    mov es:[bx+si],'  '
    add si,2
    
    mov es:[bx+si],'  '
    add si,2
    
    mov ax,ds:[bx+si]
    mov es:[bx+si],ax
    add si,2
    
    mov ax,ds:[bx+si]
    mov es:[bx+si],ax
    add si,2
    
    mov es:[bx+si],'  '
    add si,2
    
    mov es:[bx+si],'  '
    add si,2
    
    mov es:[bx+si],'  '
    add si,2
    
    mov es:[bx+si],'  '
    add si,2
    
    mov byte ptr es:[bx+si],' '
    inc si
    
    mov ax,ds:[bx+si]
    mov es:[bx+si],ax
    add si,2
    
    mov byte ptr es:[bx+si],' '
    inc si
    
    mov ax,ds:[bx+5]
    mov dx,ds:[bx+7]
    div word ptr ds:[bx+10]
    mov es:[bx+si],ax
    add si,2
    
    mov byte ptr es:[bx+si],' '
    inc si
    
    add bx,16
    loop s0

    mov ax,4c00h
    int 21h
codesg ends

end start
