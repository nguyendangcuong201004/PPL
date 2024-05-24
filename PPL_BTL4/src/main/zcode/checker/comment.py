# """
#     * Type gồm
#         * NumberType, BoolType, StringType
#         * ArrayType : gồm size, eleType (NumberType, BoolType, StringType)
#         * ArrayZcode : eleType chỉ bao gồm các type kiểu Zcode và ArrayZcode, typ chưa được suy diễn
#         * Zcode : typ chưa được suy diễn cần xác định khi lần dùng đầu tiên
#             *  FuncZcode : kiểu typ của hàm chưa suy diễn or có thể đã được suy diễn gồm
#                 ^ param : danh sách các biến cần truyền vào hàm được biểu diễn dưới dạng danh sách kiêu
#                 ^ typ : kiểu type của hàm hiện tại nếu typ là None thì hàm này chưa xác định kiểu ngược lại có typ thì đã xác định được kiểu
#                 ^ body : xem thử hàm khai báo trước 1 phần (nghĩa là không có body) hay không
#             * VarZcode : kiểu typ của biến chưa được suy diễn or có thể đã được suy diễn
#                 ^ typ : kiểu type của hàm hiện tại nếu typ là None thì biến này chưa xác định kiểu ngược lại có typ thì đã xác định được kiểu
# """
