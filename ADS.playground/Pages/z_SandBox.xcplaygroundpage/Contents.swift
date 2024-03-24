import Foundation

// Sources models, helpers, etc
import PlaygroundSupport

// MARK: - Sandbox
let queue = Queue<Int>()

for i in 1..<6 {
    print(i)
    queue.enqueue(i)
}

var ret: Int? = 0
print()
print("queue peak: \(queue.peek() ?? -1)\nqueue lenght: \(queue.length)\n")

repeat {
    if let ret = queue.dequeue() {
        print(ret)
    }
} while ret != nil
