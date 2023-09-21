# javaGetterSetter
A Python code for generating getter-setter methods of Java.
<br>
Just copy and paste the variable names with their datatype 
<br>
<br>
eg.
```
String data;
char[] letters;
static double const;
MyClass obj;
```
<br>
Result:
<br>

```
void setData(String data) {this.data=data;}
void setLetters(char[] letters) {this.letters=letters;}
void setConst(double const) {this.const=const;}
void setObj(MyClass obj) {this.obj=obj;}

String getData() {return this.data;}
char[] getLetters() {return this.letters;}
double getConst() {return this.const;}
MyClass getObj() {return this.obj;}
```

Note : 
This program ignores all the access and non-access modifiers.
<br> Ensure that input is given correctly, with the suitable proper spaces between names and datatypes;
