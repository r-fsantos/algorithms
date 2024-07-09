import Foundation

// Sources models, helpers, etc
import PlaygroundSupport

public final class Queue<T> {
    private var head: Node<T>?
    private var tail: Node<T>?
    private (set) public var length: Int

    public init(head: Node<T>? = nil, tail: Node<T>? = nil, length: Int = 0) {
        self.head = head
        self.tail = tail
        self.length = length
    }

    public func enqueue(_ item: T) -> Void {
        length += 1
        let node = Node(value: item)
        if (tail == nil) {
            head = node
            tail = head
            return
        }

        tail?.next = node
        tail = node
    }

    public func dequeue() -> T? {
        if (head == nil) {
            return nil
        }
        length -= 1

        let head = self.head
        self.head = self.head?.next

        // memory sanitizing
        head?.next = nil
        if length == 0 {
            tail = nil
        }

        return head?.value
    }

    public func peek() -> T? {
        head?.value
    }
}
