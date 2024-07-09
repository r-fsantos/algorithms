import Foundation
import XCTest

func bubbleSort(_ arr: inout [Int]) -> Void {
    for i in 0..<arr.count {
        for j in 0..<(arr.count - 1 - i) {
            if (arr[j] > arr[j + 1]) {
                let tmp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = tmp
            }
        }
    }
}

final class SolutionTest: XCTestCase {
    static var allCases = [("solution", testSolution)]

    func testSolution() {
        var arr = [9, 3, 7, 4, 69, 420, 42]
        let expArr = [3, 4, 7, 9, 42, 69, 420]

        bubbleSort(&arr)
        XCTAssertEqual(arr, expArr)
    }
}

SolutionTest.defaultTestSuite.run()
