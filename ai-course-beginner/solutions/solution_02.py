"""
Решение задания 2: Основы Машинного Обучения
Часть 3: Практическое задание с кодом
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

# Настройка стиля графиков
plt.style.use('seaborn-v0_8')
np.random.seed(42)

print("=" * 60)
print("Задание 3.1: Реализация линейной регрессии")
print("=" * 60)

# =============================================================================
# 1. Создание данных
# =============================================================================

n_samples = 100
X = np.random.uniform(20, 200, n_samples).reshape(-1, 1)  # площадь от 20 до 200 м²
true_coefficient = 50000  # 50000 рублей за м²
noise = np.random.normal(0, 500000, n_samples)  # шум со стандартным отклонением 500к
y = true_coefficient * X.flatten() + noise  # цена с шумом

print(f"\nСоздано {n_samples} точек данных")
print(f"Диапазон площади: {X.min():.1f} - {X.max():.1f} м²")
print(f"Диапазон цены: {y.min()/1e6:.1f} - {y.max()/1e6:.1f} млн руб")

# =============================================================================
# 2. Визуализация данных
# =============================================================================

plt.figure(figsize=(10, 6))
plt.scatter(X, y, alpha=0.6, s=50, color='blue', label='Данные')
plt.xlabel('Площадь (м²)', fontsize=12)
plt.ylabel('Цена (руб)', fontsize=12)
plt.title('Зависимость цены от площади', fontsize=14)
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.savefig('/workspace/ai-course-beginner/solutions/images/scatter_plot.png', dpi=150)
plt.show()

# =============================================================================
# 3. Обучение модели
# =============================================================================

model = LinearRegression()
model.fit(X, y)

print(f"\nОбучение модели завершено")
print(f"Коэффициент (вес): {model.coef_[0]:.2f} руб/м²")
print(f"Свободный член (bias): {model.intercept_:.2f} руб")
print(f"Истинный коэффициент: {true_coefficient} руб/м²")

# =============================================================================
# 4. Предсказания и визуализация
# =============================================================================

predictions = model.predict(X)

plt.figure(figsize=(10, 6))
plt.scatter(X, y, alpha=0.6, s=50, color='blue', label='Фактические данные')
plt.plot(X, predictions, color='red', linewidth=2, label='Линия регрессии')
plt.xlabel('Площадь (м²)', fontsize=12)
plt.ylabel('Цена (руб)', fontsize=12)
plt.title('Линейная регрессия: Зависимость цены от площади', fontsize=14)
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.savefig('/workspace/ai-course-beginner/solutions/images/regression_line.png', dpi=150)
plt.show()

# =============================================================================
# 5. Метрики
# =============================================================================

mse = mean_squared_error(y, predictions)
rmse = np.sqrt(mse)
r2 = r2_score(y, predictions)

print(f"\n{'='*60}")
print("Метрики качества модели")
print('='*60)
print(f"MSE (среднеквадратичная ошибка): {mse:.2f}")
print(f"RMSE (корень из MSE): {rmse:.2f} руб")
print(f"R² (коэффициент детерминации): {r2:.4f}")
print(f"R² в процентах: {r2*100:.2f}%")

# =============================================================================
# Задание 3.2: Эксперимент с параметрами
# =============================================================================

print(f"\n{'='*60}")
print("Задание 3.2: Эксперимент с параметрами")
print("="*60)

# -----------------------------------------------------------------------------
# Эксперимент 1: Больше шума
# -----------------------------------------------------------------------------

print("\n--- Эксперимент 1: Увеличенный шум ---")

noise_high = np.random.normal(0, 2000000, n_samples)  # шум в 4 раза больше
y_noisy = true_coefficient * X.flatten() + noise_high

model_noisy = LinearRegression()
model_noisy.fit(X, y_noisy)
pred_noisy = model_noisy.predict(X)

mse_noisy = mean_squared_error(y_noisy, pred_noisy)
r2_noisy = r2_score(y_noisy, pred_noisy)

print(f"MSE: {mse_noisy:.2f}")
print(f"R²: {r2_noisy:.4f} ({r2_noisy*100:.2f}%)")
print(f"Вывод: При увеличении шума R² уменьшается, модель хуже объясняет данные")

# -----------------------------------------------------------------------------
# Эксперимент 2: Меньше данных
# -----------------------------------------------------------------------------

print("\n--- Эксперимент 2: Мало данных (20 точек) ---")

n_few = 20
X_few = np.random.uniform(20, 200, n_few).reshape(-1, 1)
y_few = true_coefficient * X_few.flatten() + np.random.normal(0, 500000, n_few)

model_few = LinearRegression()
model_few.fit(X_few, y_few)
pred_few = model_few.predict(X_few)

mse_few = mean_squared_error(y_few, pred_few)
r2_few = r2_score(y_few, pred_few)

print(f"MSE: {mse_few:.2f}")
print(f"R²: {r2_few:.4f} ({r2_few*100:.2f}%)")
print(f"Вывод: С малым количеством данных метрики менее надёжны")

# -----------------------------------------------------------------------------
# Эксперимент 3: Нелинейная зависимость
# -----------------------------------------------------------------------------

print("\n--- Эксперимент 3: Нелинейная зависимость (y = x²) ---")

X_nonlin = np.random.uniform(10, 50, n_samples).reshape(-1, 1)
y_nonlin = 100 * (X_nonlin.flatten() ** 2) + np.random.normal(0, 10000, n_samples)

model_nonlin = LinearRegression()
model_nonlin.fit(X_nonlin, y_nonlin)
pred_nonlin = model_nonlin.predict(X_nonlin)

mse_nonlin = mean_squared_error(y_nonlin, pred_nonlin)
r2_nonlin = r2_score(y_nonlin, pred_nonlin)

print(f"MSE: {mse_nonlin:.2f}")
print(f"R²: {r2_nonlin:.4f} ({r2_nonlin*100:.2f}%)")
print(f"Вывод: Линейная модель плохо работает с нелинейными данными")

# Визуализация нелинейной зависимости
plt.figure(figsize=(10, 6))
plt.scatter(X_nonlin, y_nonlin, alpha=0.6, s=50, color='green', label='Данные')
plt.plot(X_nonlin, pred_nonlin, color='red', linewidth=2, label='Линейная аппроксимация')
plt.xlabel('X', fontsize=12)
plt.ylabel('Y = X²', fontsize=12)
plt.title('Нелинейная зависимость и линейная модель', fontsize=14)
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.savefig('/workspace/ai-course-beginner/solutions/images/nonlinear.png', dpi=150)
plt.show()

# =============================================================================
# Итоговые выводы
# =============================================================================

print(f"\n{'='*60}")
print("ИТОГОВЫЕ ВЫВОДЫ")
print("="*60)

print("""
1. Линейная регрессия хорошо работает, когда данные действительно имеют
   линейную зависимость (высокий R² > 0.9).

2. Увеличение шума ухудшает качество модели (снижается R²), но модель
   всё ещё находит правильный тренд.

3. Малое количество данных делает оценку метрик ненадёжной. Модель может
   случайно хорошо или плохо работать на конкретной выборке.

4. Линейная модель НЕ подходит для нелинейных зависимостей. В таких случаях
   нужно использовать:
   - Полиномиальную регрессию
   - Нейронные сети
   - Другие нелинейные алгоритмы

5. Важно всегда визуализировать данные перед выбором модели!
""")

print("\nРекомендуемые следующие шаги:")
print("- Попробуйте полиномиальную регрессию для нелинейных данных")
print("- Разделите данные на train/test для более честной оценки")
print("- Добавьте дополнительные признаки для улучшения модели")
