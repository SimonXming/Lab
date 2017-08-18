#! /bin/bash

# The C Preprocessor modifies the source code before beginning the translation to IR. 
clang -E compile_me.c -o preprocessed.i

# Run the clang frontend on compile_me.c to generate LLVM IR
clang -S -emit-llvm -o llvm_ir.ll compile_me.c

# optimizer is to improve code efficiency based on its understanding of the program’s runtime behavior.
# The optimizer takes IR as input and produces improved IR as output. 
opt -O2 -S llvm_ir.ll -o optimized.ll

# generates machine code from LLVM IR input 
llc -o compiled-assembly.s optimized.ll