import blosc
import enum


CompressionAlgorithms = enum.Enum(
    "CompressionAlgorithms", {name: name for name in blosc.cnames}
)
CompressionAlgorithms.__str__ = lambda self: self.name
