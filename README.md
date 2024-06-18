# Applied linear algebra.  
# Lab assignment 2. Eigenvalues and eigenvectors.  
  
### 1. Що таке власне значення і власний вектор матриці? Як вони обчислюються?  
*Власний вектор* — це ненульовий вектор v, для якого виконується співвідношення **Av=λv**, де λ - це певний скаляр, тобто дійсне або комплексне число.  
*Власне значення* - це скаляр, при якому рівняння **Av=λv** має ненульовий розв'язок.  
1. Розв'язуємо рівняння det(A-λI)=0, щоб знайти власні значення.  
2. Підставляємо власні значення у формулу і віднімаємо λI від матриці A.  
3. Розв'язуємо отриману матрицю як систему рівнянь та знаходимо вектор.  
4. Повторити для усіх власних значень та скласти вектори у матрицю.  

  
### 2. Які властивості мають власні вектори симетричних матриць?  
-  Всі власні значення симетричної матриці дійсні.  
-  Власні вектори, які відповідають різним власним значенням, є ортогональними.  
-  Симетричну матрицю можна діагоналізувати за допомогою ортогональної матриці.
  
  
### 3. Які можуть бути недоліки використання PCA, і які стратегії можуть використовуватися для подолання цих недоліків?  
**Недоліки PCA:**  
  
1. *Лінійність*: PCA може виявити тільки лінійні взаємозв'язки між змінними, і не може розпізнавати нелінійні структури.  
2. *Чутливість до масштабу*: PCA чутливий до масштабів даних, тому змінні з більшим діапазоном значень можуть домінувати.  
3. *Шум*: PCA може зменшити розмірність, але разом з корисною інформацією може також залишитися шум.  
4. *Інтерпретованість*: Головні компоненти можуть бути важко інтерпретувати в контексті початкових змінних.
  
**Стратегії подолання недоліків:**  
  
1. *Масштабування даних*: Нормалізація або стандартизація даних перед застосуванням PCA.  
2. *Використання нелінійних методів*: Методи, такі як Kernel PCA, можуть використовуватися для виявлення нелінійних взаємозв'язків.  
3. *Фільтрація шуму*: Попереднє видалення шуму або використання методів регуляризації.  
4. *Розширена інтерпретація*: Використання візуалізацій та аналізу для кращого розуміння головних компонент.


### 4. Які переваги має діагоналізація матриці в криптографії? Як вона застосовується для шифрування та дешифрування повідомлень?  
**Переваги діагоналізації:**  
  
1. Значно спрощує обчислення, особливо коли треба виконувати операції багаторазового піднесення до степеня.  
2. Зменшує час і ресурси, необхідні для обчислень.
   
**Застосування:**  
  
1. При шифруванні повідомлення перетворюється на вектор і множиться на матрицю.  
2. Якщо матриця діагоналізована, операції з нею стають простішими і швидшими.  
3. При дешифруванні використовують обернену матрицю для відновлення оригінального повідомлення.  