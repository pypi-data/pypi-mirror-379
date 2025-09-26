#!/usr/bin/env python3
"""
사용자 정의 클래스와 Signal 타입 검증 데모

이 예시는 사용자가 정의한 데이터 클래스가 Signal에서 올바르게 작동하는지 테스트합니다.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.eq1core.signal import Signal
from dataclasses import dataclass
from typing import List, Dict, Any


@dataclass
class UserData:
    """사용자 정의 데이터 클래스"""
    name: str
    age: int
    email: str


@dataclass
class ProductInfo:
    """제품 정보 데이터 클래스"""
    id: str
    name: str
    price: float
    category: str


class InspectionResult:
    """검사 결과 클래스"""
    def __init__(self, status: str, score: float, defects: List[str]):
        self.status = status
        self.score = score
        self.defects = defects
    
    def __str__(self):
        return f"InspectionResult(status={self.status}, score={self.score})"


def test_basic_types():
    """기본 타입 테스트"""
    print("=== 기본 타입 테스트 ===")
    
    def on_string_event(data: str):
        print(f"✅ String event: {data}")
    
    def on_int_event(number: int):
        print(f"✅ Int event: {number}")
    
    def on_dict_event(data: dict):
        print(f"✅ Dict event: {data}")
    
    # 기본 타입 Signal
    string_signal = Signal(str)
    int_signal = Signal(int)
    dict_signal = Signal(dict)
    
    string_signal.connect(on_string_event)
    int_signal.connect(on_int_event)
    dict_signal.connect(on_dict_event)
    
    string_signal.emit("Hello World")
    int_signal.emit(42)
    dict_signal.emit({"key": "value", "number": 123})
    print()


def test_custom_dataclass():
    """사용자 정의 dataclass 테스트"""
    print("=== 사용자 정의 dataclass 테스트 ===")
    
    def on_user_event(user: UserData):
        print(f"✅ User event: {user.name} ({user.age}) - {user.email}")
    
    def on_product_event(product: ProductInfo):
        print(f"✅ Product event: {product.name} - ${product.price} ({product.category})")
    
    # 사용자 정의 클래스 Signal
    user_signal = Signal(UserData)
    product_signal = Signal(ProductInfo)
    
    user_signal.connect(on_user_event)
    product_signal.connect(on_product_event)
    
    # 올바른 타입으로 emit
    user = UserData("John Doe", 30, "john@example.com")
    product = ProductInfo("P001", "Smartphone", 999.99, "Electronics")
    
    user_signal.emit(user)
    product_signal.emit(product)
    
    # 잘못된 타입으로 emit (경고 발생)
    print("\n--- 잘못된 타입 테스트 ---")
    user_signal.emit("Not a UserData object")  # 경고 발생
    product_signal.emit({"id": "P002", "name": "Laptop"})  # 경고 발생
    print()


def test_custom_class():
    """사용자 정의 클래스 테스트"""
    print("=== 사용자 정의 클래스 테스트 ===")
    
    def on_inspection_event(result: InspectionResult):
        print(f"✅ Inspection event: {result}")
        print(f"   Status: {result.status}, Score: {result.score}")
        print(f"   Defects: {result.defects}")
    
    # 사용자 정의 클래스 Signal
    inspection_signal = Signal(InspectionResult)
    inspection_signal.connect(on_inspection_event)
    
    # 올바른 타입으로 emit
    result = InspectionResult("PASS", 0.95, ["minor_scratch"])
    inspection_signal.emit(result)
    
    # 잘못된 타입으로 emit (경고 발생)
    print("\n--- 잘못된 타입 테스트 ---")
    inspection_signal.emit({"status": "FAIL", "score": 0.5})  # 경고 발생
    print()


def test_multiple_custom_types():
    """여러 사용자 정의 타입 조합 테스트"""
    print("=== 여러 사용자 정의 타입 조합 테스트 ===")
    
    def on_complex_event(user: UserData, product: ProductInfo, result: InspectionResult):
        print(f"✅ Complex event:")
        print(f"   User: {user.name}")
        print(f"   Product: {product.name}")
        print(f"   Result: {result.status}")
    
    # 여러 사용자 정의 타입 Signal
    complex_signal = Signal(UserData, ProductInfo, InspectionResult)
    complex_signal.connect(on_complex_event)
    
    # 올바른 타입으로 emit
    user = UserData("Alice", 25, "alice@example.com")
    product = ProductInfo("P003", "Tablet", 499.99, "Electronics")
    result = InspectionResult("PASS", 0.98, [])
    
    complex_signal.emit(user, product, result)
    
    # 잘못된 타입으로 emit (경고 발생)
    print("\n--- 잘못된 타입 테스트 ---")
    complex_signal.emit(user, "Not a ProductInfo", result)  # 경고 발생
    print()


def test_inheritance():
    """상속 관계 테스트"""
    print("=== 상속 관계 테스트 ===")
    
    class BaseData:
        def __init__(self, id: str):
            self.id = id
    
    class ExtendedData(BaseData):
        def __init__(self, id: str, name: str):
            super().__init__(id)
            self.name = name
    
    def on_base_event(data: BaseData):
        print(f"✅ Base event: {data.id}")
    
    def on_extended_event(data: ExtendedData):
        print(f"✅ Extended event: {data.id} - {data.name}")
    
    # 상속 관계 Signal
    base_signal = Signal(BaseData)
    extended_signal = Signal(ExtendedData)
    
    base_signal.connect(on_base_event)
    extended_signal.connect(on_extended_event)
    
    # 올바른 타입으로 emit
    base_data = BaseData("B001")
    extended_data = ExtendedData("E001", "Extended")
    
    base_signal.emit(base_data)
    extended_signal.emit(extended_data)
    
    # 상속 관계 테스트
    print("\n--- 상속 관계 테스트 ---")
    base_signal.emit(extended_data)  # ✅ ExtendedData는 BaseData의 인스턴스이므로 정상
    extended_signal.emit(base_data)  # ❌ BaseData는 ExtendedData의 인스턴스가 아니므로 경고
    print()


def main():
    """모든 테스트 실행"""
    print("🚀 사용자 정의 클래스 Signal 테스트 시작")
    print("=" * 60)
    
    test_basic_types()
    test_custom_dataclass()
    test_custom_class()
    test_multiple_custom_types()
    test_inheritance()
    
    print("✅ 모든 테스트 완료!")


if __name__ == "__main__":
    main()
