import Foundation
import XCTest

// MARK: - Implementation
func linearSearch(haystack: [Int], needle: Int) -> Bool {
    for i in 0..<haystack.count {
        if haystack[i] == needle {
            return true
        }
    }
    return false
}

// MARK: - Tests
final class SolutionTests: XCTestCase {
    static var allTests = [("solution", testSolution)]

    func testSolution() {
        let foo = [1, 3, 4, 69, 71, 81, 90, 99, 420, 1337, 69420]
        XCTAssertEqual(linearSearch(haystack: foo, needle: 69), true)
        XCTAssertEqual(linearSearch(haystack: foo, needle: 1336), false)
        XCTAssertEqual(linearSearch(haystack: foo, needle: 69420), true)
        XCTAssertEqual(linearSearch(haystack: foo, needle: 69421), false)
        XCTAssertEqual(linearSearch(haystack: foo, needle: 1), true)
        XCTAssertEqual(linearSearch(haystack: foo, needle: 0), false)
    }
}

SolutionTests.defaultTestSuite.run()
