# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\64")
        buf.write("\u017e\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\3\2\7\2T\n\2\f\2\16\2W\13\2\3\2")
        buf.write("\3\2\3\2\3\3\3\3\3\3\3\3\5\3`\n\3\3\4\3\4\3\4\3\4\5\4")
        buf.write("f\n\4\3\5\3\5\3\5\5\5k\n\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\5\7x\n\7\3\7\3\7\5\7|\n\7\3\b\3\b\3\b")
        buf.write("\3\b\5\b\u0082\n\b\3\t\3\t\3\t\3\t\5\t\u0088\n\t\3\n\3")
        buf.write("\n\3\n\3\n\5\n\u008e\n\n\3\n\3\n\5\n\u0092\n\n\3\n\3\n")
        buf.write("\5\n\u0096\n\n\3\n\3\n\5\n\u009a\n\n\3\13\3\13\3\13\3")
        buf.write("\13\3\13\5\13\u00a1\n\13\3\f\3\f\3\f\3\f\3\f\3\f\5\f\u00a9")
        buf.write("\n\f\3\r\3\r\3\16\3\16\3\16\3\16\3\16\5\16\u00b2\n\16")
        buf.write("\3\17\3\17\3\17\3\17\3\17\5\17\u00b9\n\17\3\20\3\20\3")
        buf.write("\20\3\20\3\20\5\20\u00c0\n\20\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\7\21\u00c8\n\21\f\21\16\21\u00cb\13\21\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\7\22\u00d3\n\22\f\22\16\22\u00d6")
        buf.write("\13\22\3\23\3\23\3\23\3\23\3\23\3\23\7\23\u00de\n\23\f")
        buf.write("\23\16\23\u00e1\13\23\3\24\3\24\3\24\5\24\u00e6\n\24\3")
        buf.write("\25\3\25\3\25\5\25\u00eb\n\25\3\26\3\26\5\26\u00ef\n\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\5\26\u00f6\n\26\3\27\3\27\3")
        buf.write("\27\3\27\3\27\3\27\3\27\5\27\u00ff\n\27\3\30\3\30\3\30")
        buf.write("\3\30\3\30\5\30\u0106\n\30\3\31\3\31\3\31\3\31\3\32\3")
        buf.write("\32\3\32\5\32\u010f\n\32\3\32\3\32\3\33\6\33\u0114\n\33")
        buf.write("\r\33\16\33\u0115\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3")
        buf.write("\34\3\34\5\34\u0121\n\34\3\35\3\35\3\35\5\35\u0126\n\35")
        buf.write("\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\5\37\u0135\n\37\3 \3 \3 \3 \3 \5 \u013c\n ")
        buf.write("\3 \3 \5 \u0140\n \3 \3 \5 \u0144\n \3 \5 \u0147\n \3")
        buf.write("!\3!\3!\3!\5!\u014d\n!\3\"\3\"\3\"\3\"\3\"\5\"\u0154\n")
        buf.write("\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3#\5#\u015f\n#\3#\3#\3$\3")
        buf.write("$\3$\3%\3%\3%\3&\3&\5&\u016b\n&\3&\3&\3\'\3\'\3\'\3(\3")
        buf.write("(\3(\3(\3(\3(\3)\3)\3)\3)\5)\u017c\n)\3)\2\5 \"$*\2\4")
        buf.write("\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64")
        buf.write("\668:<>@BDFHJLNP\2\7\3\2\5\7\4\2\36\37!%\3\2\27\30\3\2")
        buf.write("\31\32\3\2\33\35\2\u018c\2U\3\2\2\2\4_\3\2\2\2\6e\3\2")
        buf.write("\2\2\bj\3\2\2\2\nl\3\2\2\2\fq\3\2\2\2\16\u0081\3\2\2\2")
        buf.write("\20\u0083\3\2\2\2\22\u0089\3\2\2\2\24\u00a0\3\2\2\2\26")
        buf.write("\u00a2\3\2\2\2\30\u00aa\3\2\2\2\32\u00b1\3\2\2\2\34\u00b8")
        buf.write("\3\2\2\2\36\u00bf\3\2\2\2 \u00c1\3\2\2\2\"\u00cc\3\2\2")
        buf.write("\2$\u00d7\3\2\2\2&\u00e5\3\2\2\2(\u00ea\3\2\2\2*\u00f5")
        buf.write("\3\2\2\2,\u00fe\3\2\2\2.\u0105\3\2\2\2\60\u0107\3\2\2")
        buf.write("\2\62\u010b\3\2\2\2\64\u0113\3\2\2\2\66\u0120\3\2\2\2")
        buf.write("8\u0125\3\2\2\2:\u0129\3\2\2\2<\u0134\3\2\2\2>\u0136\3")
        buf.write("\2\2\2@\u014c\3\2\2\2B\u014e\3\2\2\2D\u0157\3\2\2\2F\u0162")
        buf.write("\3\2\2\2H\u0165\3\2\2\2J\u0168\3\2\2\2L\u016e\3\2\2\2")
        buf.write("N\u0171\3\2\2\2P\u017b\3\2\2\2RT\7/\2\2SR\3\2\2\2TW\3")
        buf.write("\2\2\2US\3\2\2\2UV\3\2\2\2VX\3\2\2\2WU\3\2\2\2XY\5\4\3")
        buf.write("\2YZ\7\2\2\3Z\3\3\2\2\2[\\\5\6\4\2\\]\5\4\3\2]`\3\2\2")
        buf.write("\2^`\5\6\4\2_[\3\2\2\2_^\3\2\2\2`\5\3\2\2\2af\5\22\n\2")
        buf.write("bc\5\b\5\2cd\5\64\33\2df\3\2\2\2ea\3\2\2\2eb\3\2\2\2f")
        buf.write("\7\3\2\2\2gk\5\n\6\2hk\5\f\7\2ik\5\20\t\2jg\3\2\2\2jh")
        buf.write("\3\2\2\2ji\3\2\2\2k\t\3\2\2\2lm\7\t\2\2mn\7,\2\2no\7 ")
        buf.write("\2\2op\5\34\17\2p\13\3\2\2\2qr\5\30\r\2rw\7,\2\2st\7\'")
        buf.write("\2\2tu\5\16\b\2uv\7(\2\2vx\3\2\2\2ws\3\2\2\2wx\3\2\2\2")
        buf.write("x{\3\2\2\2yz\7 \2\2z|\5\34\17\2{y\3\2\2\2{|\3\2\2\2|\r")
        buf.write("\3\2\2\2}~\7-\2\2~\177\7+\2\2\177\u0082\5\16\b\2\u0080")
        buf.write("\u0082\7-\2\2\u0081}\3\2\2\2\u0081\u0080\3\2\2\2\u0082")
        buf.write("\17\3\2\2\2\u0083\u0084\7\n\2\2\u0084\u0087\7,\2\2\u0085")
        buf.write("\u0086\7 \2\2\u0086\u0088\5\34\17\2\u0087\u0085\3\2\2")
        buf.write("\2\u0087\u0088\3\2\2\2\u0088\21\3\2\2\2\u0089\u008a\7")
        buf.write("\13\2\2\u008a\u008b\7,\2\2\u008b\u008d\7)\2\2\u008c\u008e")
        buf.write("\5\24\13\2\u008d\u008c\3\2\2\2\u008d\u008e\3\2\2\2\u008e")
        buf.write("\u008f\3\2\2\2\u008f\u0099\7*\2\2\u0090\u0092\5\64\33")
        buf.write("\2\u0091\u0090\3\2\2\2\u0091\u0092\3\2\2\2\u0092\u0093")
        buf.write("\3\2\2\2\u0093\u009a\5J&\2\u0094\u0096\5\64\33\2\u0095")
        buf.write("\u0094\3\2\2\2\u0095\u0096\3\2\2\2\u0096\u0097\3\2\2\2")
        buf.write("\u0097\u009a\5N(\2\u0098\u009a\5\64\33\2\u0099\u0091\3")
        buf.write("\2\2\2\u0099\u0095\3\2\2\2\u0099\u0098\3\2\2\2\u009a\23")
        buf.write("\3\2\2\2\u009b\u009c\5\26\f\2\u009c\u009d\7+\2\2\u009d")
        buf.write("\u009e\5\24\13\2\u009e\u00a1\3\2\2\2\u009f\u00a1\5\26")
        buf.write("\f\2\u00a0\u009b\3\2\2\2\u00a0\u009f\3\2\2\2\u00a1\25")
        buf.write("\3\2\2\2\u00a2\u00a3\5\30\r\2\u00a3\u00a8\7,\2\2\u00a4")
        buf.write("\u00a5\7\'\2\2\u00a5\u00a6\5\16\b\2\u00a6\u00a7\7(\2\2")
        buf.write("\u00a7\u00a9\3\2\2\2\u00a8\u00a4\3\2\2\2\u00a8\u00a9\3")
        buf.write("\2\2\2\u00a9\27\3\2\2\2\u00aa\u00ab\t\2\2\2\u00ab\31\3")
        buf.write("\2\2\2\u00ac\u00ad\5\34\17\2\u00ad\u00ae\7+\2\2\u00ae")
        buf.write("\u00af\5\32\16\2\u00af\u00b2\3\2\2\2\u00b0\u00b2\5\34")
        buf.write("\17\2\u00b1\u00ac\3\2\2\2\u00b1\u00b0\3\2\2\2\u00b2\33")
        buf.write("\3\2\2\2\u00b3\u00b4\5\36\20\2\u00b4\u00b5\7&\2\2\u00b5")
        buf.write("\u00b6\5\36\20\2\u00b6\u00b9\3\2\2\2\u00b7\u00b9\5\36")
        buf.write("\20\2\u00b8\u00b3\3\2\2\2\u00b8\u00b7\3\2\2\2\u00b9\35")
        buf.write("\3\2\2\2\u00ba\u00bb\5 \21\2\u00bb\u00bc\t\3\2\2\u00bc")
        buf.write("\u00bd\5 \21\2\u00bd\u00c0\3\2\2\2\u00be\u00c0\5 \21\2")
        buf.write("\u00bf\u00ba\3\2\2\2\u00bf\u00be\3\2\2\2\u00c0\37\3\2")
        buf.write("\2\2\u00c1\u00c2\b\21\1\2\u00c2\u00c3\5\"\22\2\u00c3\u00c9")
        buf.write("\3\2\2\2\u00c4\u00c5\f\4\2\2\u00c5\u00c6\t\4\2\2\u00c6")
        buf.write("\u00c8\5\"\22\2\u00c7\u00c4\3\2\2\2\u00c8\u00cb\3\2\2")
        buf.write("\2\u00c9\u00c7\3\2\2\2\u00c9\u00ca\3\2\2\2\u00ca!\3\2")
        buf.write("\2\2\u00cb\u00c9\3\2\2\2\u00cc\u00cd\b\22\1\2\u00cd\u00ce")
        buf.write("\5$\23\2\u00ce\u00d4\3\2\2\2\u00cf\u00d0\f\4\2\2\u00d0")
        buf.write("\u00d1\t\5\2\2\u00d1\u00d3\5$\23\2\u00d2\u00cf\3\2\2\2")
        buf.write("\u00d3\u00d6\3\2\2\2\u00d4\u00d2\3\2\2\2\u00d4\u00d5\3")
        buf.write("\2\2\2\u00d5#\3\2\2\2\u00d6\u00d4\3\2\2\2\u00d7\u00d8")
        buf.write("\b\23\1\2\u00d8\u00d9\5&\24\2\u00d9\u00df\3\2\2\2\u00da")
        buf.write("\u00db\f\4\2\2\u00db\u00dc\t\6\2\2\u00dc\u00de\5&\24\2")
        buf.write("\u00dd\u00da\3\2\2\2\u00de\u00e1\3\2\2\2\u00df\u00dd\3")
        buf.write("\2\2\2\u00df\u00e0\3\2\2\2\u00e0%\3\2\2\2\u00e1\u00df")
        buf.write("\3\2\2\2\u00e2\u00e3\7\26\2\2\u00e3\u00e6\5&\24\2\u00e4")
        buf.write("\u00e6\5(\25\2\u00e5\u00e2\3\2\2\2\u00e5\u00e4\3\2\2\2")
        buf.write("\u00e6\'\3\2\2\2\u00e7\u00e8\t\5\2\2\u00e8\u00eb\5(\25")
        buf.write("\2\u00e9\u00eb\5*\26\2\u00ea\u00e7\3\2\2\2\u00ea\u00e9")
        buf.write("\3\2\2\2\u00eb)\3\2\2\2\u00ec\u00ef\7,\2\2\u00ed\u00ef")
        buf.write("\5\62\32\2\u00ee\u00ec\3\2\2\2\u00ee\u00ed\3\2\2\2\u00ef")
        buf.write("\u00f0\3\2\2\2\u00f0\u00f1\7\'\2\2\u00f1\u00f2\5\32\16")
        buf.write("\2\u00f2\u00f3\7(\2\2\u00f3\u00f6\3\2\2\2\u00f4\u00f6")
        buf.write("\5,\27\2\u00f5\u00ee\3\2\2\2\u00f5\u00f4\3\2\2\2\u00f6")
        buf.write("+\3\2\2\2\u00f7\u00ff\7,\2\2\u00f8\u00ff\5.\30\2\u00f9")
        buf.write("\u00fa\7)\2\2\u00fa\u00fb\5\34\17\2\u00fb\u00fc\7*\2\2")
        buf.write("\u00fc\u00ff\3\2\2\2\u00fd\u00ff\5\62\32\2\u00fe\u00f7")
        buf.write("\3\2\2\2\u00fe\u00f8\3\2\2\2\u00fe\u00f9\3\2\2\2\u00fe")
        buf.write("\u00fd\3\2\2\2\u00ff-\3\2\2\2\u0100\u0106\7-\2\2\u0101")
        buf.write("\u0106\7.\2\2\u0102\u0106\7\3\2\2\u0103\u0106\7\4\2\2")
        buf.write("\u0104\u0106\5\60\31\2\u0105\u0100\3\2\2\2\u0105\u0101")
        buf.write("\3\2\2\2\u0105\u0102\3\2\2\2\u0105\u0103\3\2\2\2\u0105")
        buf.write("\u0104\3\2\2\2\u0106/\3\2\2\2\u0107\u0108\7\'\2\2\u0108")
        buf.write("\u0109\5\32\16\2\u0109\u010a\7(\2\2\u010a\61\3\2\2\2\u010b")
        buf.write("\u010c\7,\2\2\u010c\u010e\7)\2\2\u010d\u010f\5\32\16\2")
        buf.write("\u010e\u010d\3\2\2\2\u010e\u010f\3\2\2\2\u010f\u0110\3")
        buf.write("\2\2\2\u0110\u0111\7*\2\2\u0111\63\3\2\2\2\u0112\u0114")
        buf.write("\7/\2\2\u0113\u0112\3\2\2\2\u0114\u0115\3\2\2\2\u0115")
        buf.write("\u0113\3\2\2\2\u0115\u0116\3\2\2\2\u0116\65\3\2\2\2\u0117")
        buf.write("\u0121\58\35\2\u0118\u0121\5:\36\2\u0119\u0121\5> \2\u011a")
        buf.write("\u0121\5D#\2\u011b\u0121\5F$\2\u011c\u0121\5H%\2\u011d")
        buf.write("\u0121\5J&\2\u011e\u0121\5L\'\2\u011f\u0121\5N(\2\u0120")
        buf.write("\u0117\3\2\2\2\u0120\u0118\3\2\2\2\u0120\u0119\3\2\2\2")
        buf.write("\u0120\u011a\3\2\2\2\u0120\u011b\3\2\2\2\u0120\u011c\3")
        buf.write("\2\2\2\u0120\u011d\3\2\2\2\u0120\u011e\3\2\2\2\u0120\u011f")
        buf.write("\3\2\2\2\u0121\67\3\2\2\2\u0122\u0126\5\n\6\2\u0123\u0126")
        buf.write("\5\f\7\2\u0124\u0126\5\20\t\2\u0125\u0122\3\2\2\2\u0125")
        buf.write("\u0123\3\2\2\2\u0125\u0124\3\2\2\2\u0126\u0127\3\2\2\2")
        buf.write("\u0127\u0128\5\64\33\2\u01289\3\2\2\2\u0129\u012a\5<\37")
        buf.write("\2\u012a\u012b\7 \2\2\u012b\u012c\5\34\17\2\u012c\u012d")
        buf.write("\5\64\33\2\u012d;\3\2\2\2\u012e\u012f\7,\2\2\u012f\u0130")
        buf.write("\7\'\2\2\u0130\u0131\5\32\16\2\u0131\u0132\7(\2\2\u0132")
        buf.write("\u0135\3\2\2\2\u0133\u0135\7,\2\2\u0134\u012e\3\2\2\2")
        buf.write("\u0134\u0133\3\2\2\2\u0135=\3\2\2\2\u0136\u0137\7\21\2")
        buf.write("\2\u0137\u0138\7)\2\2\u0138\u0139\5\34\17\2\u0139\u013b")
        buf.write("\7*\2\2\u013a\u013c\5\64\33\2\u013b\u013a\3\2\2\2\u013b")
        buf.write("\u013c\3\2\2\2\u013c\u013d\3\2\2\2\u013d\u013f\5\66\34")
        buf.write("\2\u013e\u0140\5@!\2\u013f\u013e\3\2\2\2\u013f\u0140\3")
        buf.write("\2\2\2\u0140\u0146\3\2\2\2\u0141\u0143\7\22\2\2\u0142")
        buf.write("\u0144\5\64\33\2\u0143\u0142\3\2\2\2\u0143\u0144\3\2\2")
        buf.write("\2\u0144\u0145\3\2\2\2\u0145\u0147\5\66\34\2\u0146\u0141")
        buf.write("\3\2\2\2\u0146\u0147\3\2\2\2\u0147?\3\2\2\2\u0148\u0149")
        buf.write("\5B\"\2\u0149\u014a\5@!\2\u014a\u014d\3\2\2\2\u014b\u014d")
        buf.write("\5B\"\2\u014c\u0148\3\2\2\2\u014c\u014b\3\2\2\2\u014d")
        buf.write("A\3\2\2\2\u014e\u014f\7\23\2\2\u014f\u0150\7)\2\2\u0150")
        buf.write("\u0151\5\34\17\2\u0151\u0153\7*\2\2\u0152\u0154\5\64\33")
        buf.write("\2\u0153\u0152\3\2\2\2\u0153\u0154\3\2\2\2\u0154\u0155")
        buf.write("\3\2\2\2\u0155\u0156\5\66\34\2\u0156C\3\2\2\2\u0157\u0158")
        buf.write("\7\f\2\2\u0158\u0159\7,\2\2\u0159\u015a\7\r\2\2\u015a")
        buf.write("\u015b\5\34\17\2\u015b\u015c\7\16\2\2\u015c\u015e\5\34")
        buf.write("\17\2\u015d\u015f\5\64\33\2\u015e\u015d\3\2\2\2\u015e")
        buf.write("\u015f\3\2\2\2\u015f\u0160\3\2\2\2\u0160\u0161\5\66\34")
        buf.write("\2\u0161E\3\2\2\2\u0162\u0163\7\17\2\2\u0163\u0164\5\64")
        buf.write("\33\2\u0164G\3\2\2\2\u0165\u0166\7\20\2\2\u0166\u0167")
        buf.write("\5\64\33\2\u0167I\3\2\2\2\u0168\u016a\7\b\2\2\u0169\u016b")
        buf.write("\5\34\17\2\u016a\u0169\3\2\2\2\u016a\u016b\3\2\2\2\u016b")
        buf.write("\u016c\3\2\2\2\u016c\u016d\5\64\33\2\u016dK\3\2\2\2\u016e")
        buf.write("\u016f\5\62\32\2\u016f\u0170\5\64\33\2\u0170M\3\2\2\2")
        buf.write("\u0171\u0172\7\24\2\2\u0172\u0173\5\64\33\2\u0173\u0174")
        buf.write("\5P)\2\u0174\u0175\7\25\2\2\u0175\u0176\5\64\33\2\u0176")
        buf.write("O\3\2\2\2\u0177\u0178\5\66\34\2\u0178\u0179\5P)\2\u0179")
        buf.write("\u017c\3\2\2\2\u017a\u017c\3\2\2\2\u017b\u0177\3\2\2\2")
        buf.write("\u017b\u017a\3\2\2\2\u017cQ\3\2\2\2*U_ejw{\u0081\u0087")
        buf.write("\u008d\u0091\u0095\u0099\u00a0\u00a8\u00b1\u00b8\u00bf")
        buf.write("\u00c9\u00d4\u00df\u00e5\u00ea\u00ee\u00f5\u00fe\u0105")
        buf.write("\u010e\u0115\u0120\u0125\u0134\u013b\u013f\u0143\u0146")
        buf.write("\u014c\u0153\u015e\u016a\u017b")
        return buf.getvalue()


class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'true'", "'false'", "'number'", "'bool'", 
                     "'string'", "'return'", "'var'", "'dynamic'", "'func'", 
                     "'for'", "'until'", "'by'", "'break'", "'continue'", 
                     "'if'", "'else'", "'elif'", "'begin'", "'end'", "'not'", 
                     "'and'", "'or'", "'+'", "'-'", "'*'", "'/'", "'%'", 
                     "'='", "'!='", "'<-'", "'<'", "'<='", "'>'", "'>='", 
                     "'=='", "'...'", "'['", "']'", "'('", "')'", "','" ]

    symbolicNames = [ "<INVALID>", "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", 
                      "RETURN", "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", 
                      "BY", "BREAK", "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", 
                      "END", "NOT", "AND", "OR", "ADD", "SUB", "MUL", "DIV", 
                      "MOD", "EQUAL", "NOT_EQUAL", "ASSIGNINIT", "LESS_THAN", 
                      "LESS_THAN_EQUAL", "GREATER_THAN", "GREATER_THAN_EQUAL", 
                      "STRING_EQUAL", "STRING_CONCAT", "LBRACKET", "RBRACKET", 
                      "LPAREN", "RPAREN", "COMMA", "ID", "NUMBER_LIT", "STRING_LIT", 
                      "NEWLINE", "COMMENTS", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                      "ERROR_CHAR" ]

    RULE_program = 0
    RULE_list_declared = 1
    RULE_declared = 2
    RULE_variables = 3
    RULE_implicit_var = 4
    RULE_keyword_var = 5
    RULE_list_NUMBER_LIT = 6
    RULE_implicit_dynamic = 7
    RULE_function = 8
    RULE_parameters_list = 9
    RULE_parameter = 10
    RULE_typ = 11
    RULE_list_expression = 12
    RULE_expression = 13
    RULE_expr1 = 14
    RULE_expr2 = 15
    RULE_expr3 = 16
    RULE_expr4 = 17
    RULE_expr5 = 18
    RULE_expr6 = 19
    RULE_expr7 = 20
    RULE_expr8 = 21
    RULE_literal = 22
    RULE_array_literal = 23
    RULE_func_call = 24
    RULE_ignore = 25
    RULE_statement = 26
    RULE_declaration_statement = 27
    RULE_assignment_statement = 28
    RULE_lhs = 29
    RULE_if_statement = 30
    RULE_elif_list = 31
    RULE_elif_stmt = 32
    RULE_for_statement = 33
    RULE_break_statement = 34
    RULE_continue_statement = 35
    RULE_return_statement = 36
    RULE_call_statement = 37
    RULE_block_statement = 38
    RULE_stmt_list = 39

    ruleNames =  [ "program", "list_declared", "declared", "variables", 
                   "implicit_var", "keyword_var", "list_NUMBER_LIT", "implicit_dynamic", 
                   "function", "parameters_list", "parameter", "typ", "list_expression", 
                   "expression", "expr1", "expr2", "expr3", "expr4", "expr5", 
                   "expr6", "expr7", "expr8", "literal", "array_literal", 
                   "func_call", "ignore", "statement", "declaration_statement", 
                   "assignment_statement", "lhs", "if_statement", "elif_list", 
                   "elif_stmt", "for_statement", "break_statement", "continue_statement", 
                   "return_statement", "call_statement", "block_statement", 
                   "stmt_list" ]

    EOF = Token.EOF
    TRUE=1
    FALSE=2
    NUMBER=3
    BOOL=4
    STRING=5
    RETURN=6
    VAR=7
    DYNAMIC=8
    FUNC=9
    FOR=10
    UNTIL=11
    BY=12
    BREAK=13
    CONTINUE=14
    IF=15
    ELSE=16
    ELIF=17
    BEGIN=18
    END=19
    NOT=20
    AND=21
    OR=22
    ADD=23
    SUB=24
    MUL=25
    DIV=26
    MOD=27
    EQUAL=28
    NOT_EQUAL=29
    ASSIGNINIT=30
    LESS_THAN=31
    LESS_THAN_EQUAL=32
    GREATER_THAN=33
    GREATER_THAN_EQUAL=34
    STRING_EQUAL=35
    STRING_CONCAT=36
    LBRACKET=37
    RBRACKET=38
    LPAREN=39
    RPAREN=40
    COMMA=41
    ID=42
    NUMBER_LIT=43
    STRING_LIT=44
    NEWLINE=45
    COMMENTS=46
    WS=47
    UNCLOSE_STRING=48
    ILLEGAL_ESCAPE=49
    ERROR_CHAR=50

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_declared(self):
            return self.getTypedRuleContext(ZCodeParser.List_declaredContext,0)


        def EOF(self):
            return self.getToken(ZCodeParser.EOF, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ZCodeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZCodeParser.NEWLINE:
                self.state = 80
                self.match(ZCodeParser.NEWLINE)
                self.state = 85
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 86
            self.list_declared()
            self.state = 87
            self.match(ZCodeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_declaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declared(self):
            return self.getTypedRuleContext(ZCodeParser.DeclaredContext,0)


        def list_declared(self):
            return self.getTypedRuleContext(ZCodeParser.List_declaredContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_list_declared

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_declared" ):
                return visitor.visitList_declared(self)
            else:
                return visitor.visitChildren(self)




    def list_declared(self):

        localctx = ZCodeParser.List_declaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_list_declared)
        try:
            self.state = 93
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 89
                self.declared()
                self.state = 90
                self.list_declared()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 92
                self.declared()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function(self):
            return self.getTypedRuleContext(ZCodeParser.FunctionContext,0)


        def variables(self):
            return self.getTypedRuleContext(ZCodeParser.VariablesContext,0)


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_declared

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclared" ):
                return visitor.visitDeclared(self)
            else:
                return visitor.visitChildren(self)




    def declared(self):

        localctx = ZCodeParser.DeclaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declared)
        try:
            self.state = 99
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.FUNC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 95
                self.function()
                pass
            elif token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.VAR, ZCodeParser.DYNAMIC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 96
                self.variables()
                self.state = 97
                self.ignore()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariablesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def implicit_var(self):
            return self.getTypedRuleContext(ZCodeParser.Implicit_varContext,0)


        def keyword_var(self):
            return self.getTypedRuleContext(ZCodeParser.Keyword_varContext,0)


        def implicit_dynamic(self):
            return self.getTypedRuleContext(ZCodeParser.Implicit_dynamicContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_variables

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariables" ):
                return visitor.visitVariables(self)
            else:
                return visitor.visitChildren(self)




    def variables(self):

        localctx = ZCodeParser.VariablesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_variables)
        try:
            self.state = 104
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 101
                self.implicit_var()
                pass
            elif token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 102
                self.keyword_var()
                pass
            elif token in [ZCodeParser.DYNAMIC]:
                self.enterOuterAlt(localctx, 3)
                self.state = 103
                self.implicit_dynamic()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Implicit_varContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(ZCodeParser.VAR, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def ASSIGNINIT(self):
            return self.getToken(ZCodeParser.ASSIGNINIT, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_implicit_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImplicit_var" ):
                return visitor.visitImplicit_var(self)
            else:
                return visitor.visitChildren(self)




    def implicit_var(self):

        localctx = ZCodeParser.Implicit_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_implicit_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(ZCodeParser.VAR)
            self.state = 107
            self.match(ZCodeParser.ID)
            self.state = 108
            self.match(ZCodeParser.ASSIGNINIT)
            self.state = 109
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Keyword_varContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(ZCodeParser.TypContext,0)


        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def LBRACKET(self):
            return self.getToken(ZCodeParser.LBRACKET, 0)

        def list_NUMBER_LIT(self):
            return self.getTypedRuleContext(ZCodeParser.List_NUMBER_LITContext,0)


        def RBRACKET(self):
            return self.getToken(ZCodeParser.RBRACKET, 0)

        def ASSIGNINIT(self):
            return self.getToken(ZCodeParser.ASSIGNINIT, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_keyword_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKeyword_var" ):
                return visitor.visitKeyword_var(self)
            else:
                return visitor.visitChildren(self)




    def keyword_var(self):

        localctx = ZCodeParser.Keyword_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_keyword_var)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self.typ()
            self.state = 112
            self.match(ZCodeParser.ID)
            self.state = 117
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.LBRACKET:
                self.state = 113
                self.match(ZCodeParser.LBRACKET)
                self.state = 114
                self.list_NUMBER_LIT()
                self.state = 115
                self.match(ZCodeParser.RBRACKET)


            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.ASSIGNINIT:
                self.state = 119
                self.match(ZCodeParser.ASSIGNINIT)
                self.state = 120
                self.expression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_NUMBER_LITContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER_LIT(self):
            return self.getToken(ZCodeParser.NUMBER_LIT, 0)

        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def list_NUMBER_LIT(self):
            return self.getTypedRuleContext(ZCodeParser.List_NUMBER_LITContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_list_NUMBER_LIT

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_NUMBER_LIT" ):
                return visitor.visitList_NUMBER_LIT(self)
            else:
                return visitor.visitChildren(self)




    def list_NUMBER_LIT(self):

        localctx = ZCodeParser.List_NUMBER_LITContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_list_NUMBER_LIT)
        try:
            self.state = 127
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 123
                self.match(ZCodeParser.NUMBER_LIT)
                self.state = 124
                self.match(ZCodeParser.COMMA)
                self.state = 125
                self.list_NUMBER_LIT()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 126
                self.match(ZCodeParser.NUMBER_LIT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Implicit_dynamicContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DYNAMIC(self):
            return self.getToken(ZCodeParser.DYNAMIC, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def ASSIGNINIT(self):
            return self.getToken(ZCodeParser.ASSIGNINIT, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_implicit_dynamic

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImplicit_dynamic" ):
                return visitor.visitImplicit_dynamic(self)
            else:
                return visitor.visitChildren(self)




    def implicit_dynamic(self):

        localctx = ZCodeParser.Implicit_dynamicContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_implicit_dynamic)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.match(ZCodeParser.DYNAMIC)
            self.state = 130
            self.match(ZCodeParser.ID)
            self.state = 133
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.ASSIGNINIT:
                self.state = 131
                self.match(ZCodeParser.ASSIGNINIT)
                self.state = 132
                self.expression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(ZCodeParser.FUNC, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def LPAREN(self):
            return self.getToken(ZCodeParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(ZCodeParser.RPAREN, 0)

        def return_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Return_statementContext,0)


        def block_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Block_statementContext,0)


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def parameters_list(self):
            return self.getTypedRuleContext(ZCodeParser.Parameters_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_function

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction" ):
                return visitor.visitFunction(self)
            else:
                return visitor.visitChildren(self)




    def function(self):

        localctx = ZCodeParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.match(ZCodeParser.FUNC)
            self.state = 136
            self.match(ZCodeParser.ID)
            self.state = 137
            self.match(ZCodeParser.LPAREN)
            self.state = 139
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STRING))) != 0):
                self.state = 138
                self.parameters_list()


            self.state = 141
            self.match(ZCodeParser.RPAREN)
            self.state = 151
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 143
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.NEWLINE:
                    self.state = 142
                    self.ignore()


                self.state = 145
                self.return_statement()
                pass

            elif la_ == 2:
                self.state = 147
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.NEWLINE:
                    self.state = 146
                    self.ignore()


                self.state = 149
                self.block_statement()
                pass

            elif la_ == 3:
                self.state = 150
                self.ignore()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parameters_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self):
            return self.getTypedRuleContext(ZCodeParser.ParameterContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def parameters_list(self):
            return self.getTypedRuleContext(ZCodeParser.Parameters_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_parameters_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameters_list" ):
                return visitor.visitParameters_list(self)
            else:
                return visitor.visitChildren(self)




    def parameters_list(self):

        localctx = ZCodeParser.Parameters_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_parameters_list)
        try:
            self.state = 158
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 153
                self.parameter()
                self.state = 154
                self.match(ZCodeParser.COMMA)
                self.state = 155
                self.parameters_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 157
                self.parameter()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(ZCodeParser.TypContext,0)


        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def LBRACKET(self):
            return self.getToken(ZCodeParser.LBRACKET, 0)

        def list_NUMBER_LIT(self):
            return self.getTypedRuleContext(ZCodeParser.List_NUMBER_LITContext,0)


        def RBRACKET(self):
            return self.getToken(ZCodeParser.RBRACKET, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_parameter

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter" ):
                return visitor.visitParameter(self)
            else:
                return visitor.visitChildren(self)




    def parameter(self):

        localctx = ZCodeParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_parameter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.typ()
            self.state = 161
            self.match(ZCodeParser.ID)
            self.state = 166
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.LBRACKET:
                self.state = 162
                self.match(ZCodeParser.LBRACKET)
                self.state = 163
                self.list_NUMBER_LIT()
                self.state = 164
                self.match(ZCodeParser.RBRACKET)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOL(self):
            return self.getToken(ZCodeParser.BOOL, 0)

        def NUMBER(self):
            return self.getToken(ZCodeParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(ZCodeParser.STRING, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_typ

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTyp" ):
                return visitor.visitTyp(self)
            else:
                return visitor.visitChildren(self)




    def typ(self):

        localctx = ZCodeParser.TypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_typ)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def list_expression(self):
            return self.getTypedRuleContext(ZCodeParser.List_expressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_list_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_expression" ):
                return visitor.visitList_expression(self)
            else:
                return visitor.visitChildren(self)




    def list_expression(self):

        localctx = ZCodeParser.List_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_list_expression)
        try:
            self.state = 175
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 170
                self.expression()
                self.state = 171
                self.match(ZCodeParser.COMMA)
                self.state = 172
                self.list_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 174
                self.expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Expr1Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expr1Context,i)


        def STRING_CONCAT(self):
            return self.getToken(ZCodeParser.STRING_CONCAT, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = ZCodeParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_expression)
        try:
            self.state = 182
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 177
                self.expr1()
                self.state = 178
                self.match(ZCodeParser.STRING_CONCAT)
                self.state = 179
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 181
                self.expr1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Expr2Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expr2Context,i)


        def EQUAL(self):
            return self.getToken(ZCodeParser.EQUAL, 0)

        def STRING_EQUAL(self):
            return self.getToken(ZCodeParser.STRING_EQUAL, 0)

        def NOT_EQUAL(self):
            return self.getToken(ZCodeParser.NOT_EQUAL, 0)

        def LESS_THAN(self):
            return self.getToken(ZCodeParser.LESS_THAN, 0)

        def GREATER_THAN(self):
            return self.getToken(ZCodeParser.GREATER_THAN, 0)

        def LESS_THAN_EQUAL(self):
            return self.getToken(ZCodeParser.LESS_THAN_EQUAL, 0)

        def GREATER_THAN_EQUAL(self):
            return self.getToken(ZCodeParser.GREATER_THAN_EQUAL, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr1" ):
                return visitor.visitExpr1(self)
            else:
                return visitor.visitChildren(self)




    def expr1(self):

        localctx = ZCodeParser.Expr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_expr1)
        self._la = 0 # Token type
        try:
            self.state = 189
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 184
                self.expr2(0)
                self.state = 185
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.EQUAL) | (1 << ZCodeParser.NOT_EQUAL) | (1 << ZCodeParser.LESS_THAN) | (1 << ZCodeParser.LESS_THAN_EQUAL) | (1 << ZCodeParser.GREATER_THAN) | (1 << ZCodeParser.GREATER_THAN_EQUAL) | (1 << ZCodeParser.STRING_EQUAL))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 186
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 188
                self.expr2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self):
            return self.getTypedRuleContext(ZCodeParser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(ZCodeParser.Expr2Context,0)


        def AND(self):
            return self.getToken(ZCodeParser.AND, 0)

        def OR(self):
            return self.getToken(ZCodeParser.OR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr2" ):
                return visitor.visitExpr2(self)
            else:
                return visitor.visitChildren(self)



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 199
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 194
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 195
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.AND or _la==ZCodeParser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 196
                    self.expr3(0) 
                self.state = 201
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self):
            return self.getTypedRuleContext(ZCodeParser.Expr4Context,0)


        def expr3(self):
            return self.getTypedRuleContext(ZCodeParser.Expr3Context,0)


        def ADD(self):
            return self.getToken(ZCodeParser.ADD, 0)

        def SUB(self):
            return self.getToken(ZCodeParser.SUB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr3" ):
                return visitor.visitExpr3(self)
            else:
                return visitor.visitChildren(self)



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 210
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 205
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 206
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.ADD or _la==ZCodeParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 207
                    self.expr4(0) 
                self.state = 212
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(ZCodeParser.Expr5Context,0)


        def expr4(self):
            return self.getTypedRuleContext(ZCodeParser.Expr4Context,0)


        def MUL(self):
            return self.getToken(ZCodeParser.MUL, 0)

        def DIV(self):
            return self.getToken(ZCodeParser.DIV, 0)

        def MOD(self):
            return self.getToken(ZCodeParser.MOD, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr4" ):
                return visitor.visitExpr4(self)
            else:
                return visitor.visitChildren(self)



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 34
        self.enterRecursionRule(localctx, 34, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 221
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 216
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 217
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.MUL) | (1 << ZCodeParser.DIV) | (1 << ZCodeParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 218
                    self.expr5() 
                self.state = 223
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(ZCodeParser.NOT, 0)

        def expr5(self):
            return self.getTypedRuleContext(ZCodeParser.Expr5Context,0)


        def expr6(self):
            return self.getTypedRuleContext(ZCodeParser.Expr6Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr5" ):
                return visitor.visitExpr5(self)
            else:
                return visitor.visitChildren(self)




    def expr5(self):

        localctx = ZCodeParser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_expr5)
        try:
            self.state = 227
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 224
                self.match(ZCodeParser.NOT)
                self.state = 225
                self.expr5()
                pass
            elif token in [ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.ADD, ZCodeParser.SUB, ZCodeParser.LBRACKET, ZCodeParser.LPAREN, ZCodeParser.ID, ZCodeParser.NUMBER_LIT, ZCodeParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 226
                self.expr6()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr6(self):
            return self.getTypedRuleContext(ZCodeParser.Expr6Context,0)


        def SUB(self):
            return self.getToken(ZCodeParser.SUB, 0)

        def ADD(self):
            return self.getToken(ZCodeParser.ADD, 0)

        def expr7(self):
            return self.getTypedRuleContext(ZCodeParser.Expr7Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr6" ):
                return visitor.visitExpr6(self)
            else:
                return visitor.visitChildren(self)




    def expr6(self):

        localctx = ZCodeParser.Expr6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_expr6)
        self._la = 0 # Token type
        try:
            self.state = 232
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.ADD, ZCodeParser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 229
                _la = self._input.LA(1)
                if not(_la==ZCodeParser.ADD or _la==ZCodeParser.SUB):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 230
                self.expr6()
                pass
            elif token in [ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.LBRACKET, ZCodeParser.LPAREN, ZCodeParser.ID, ZCodeParser.NUMBER_LIT, ZCodeParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 231
                self.expr7()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACKET(self):
            return self.getToken(ZCodeParser.LBRACKET, 0)

        def RBRACKET(self):
            return self.getToken(ZCodeParser.RBRACKET, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def func_call(self):
            return self.getTypedRuleContext(ZCodeParser.Func_callContext,0)


        def list_expression(self):
            return self.getTypedRuleContext(ZCodeParser.List_expressionContext,0)


        def expr8(self):
            return self.getTypedRuleContext(ZCodeParser.Expr8Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr7" ):
                return visitor.visitExpr7(self)
            else:
                return visitor.visitChildren(self)




    def expr7(self):

        localctx = ZCodeParser.Expr7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_expr7)
        try:
            self.state = 243
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 236
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
                if la_ == 1:
                    self.state = 234
                    self.match(ZCodeParser.ID)
                    pass

                elif la_ == 2:
                    self.state = 235
                    self.func_call()
                    pass


                self.state = 238
                self.match(ZCodeParser.LBRACKET)

                self.state = 239
                self.list_expression()
                self.state = 240
                self.match(ZCodeParser.RBRACKET)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 242
                self.expr8()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr8Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def literal(self):
            return self.getTypedRuleContext(ZCodeParser.LiteralContext,0)


        def LPAREN(self):
            return self.getToken(ZCodeParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(ZCodeParser.RPAREN, 0)

        def func_call(self):
            return self.getTypedRuleContext(ZCodeParser.Func_callContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr8" ):
                return visitor.visitExpr8(self)
            else:
                return visitor.visitChildren(self)




    def expr8(self):

        localctx = ZCodeParser.Expr8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_expr8)
        try:
            self.state = 252
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 245
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 246
                self.literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 247
                self.match(ZCodeParser.LPAREN)
                self.state = 248
                self.expression()
                self.state = 249
                self.match(ZCodeParser.RPAREN)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 251
                self.func_call()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER_LIT(self):
            return self.getToken(ZCodeParser.NUMBER_LIT, 0)

        def STRING_LIT(self):
            return self.getToken(ZCodeParser.STRING_LIT, 0)

        def TRUE(self):
            return self.getToken(ZCodeParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(ZCodeParser.FALSE, 0)

        def array_literal(self):
            return self.getTypedRuleContext(ZCodeParser.Array_literalContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = ZCodeParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_literal)
        try:
            self.state = 259
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 254
                self.match(ZCodeParser.NUMBER_LIT)
                pass
            elif token in [ZCodeParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 255
                self.match(ZCodeParser.STRING_LIT)
                pass
            elif token in [ZCodeParser.TRUE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 256
                self.match(ZCodeParser.TRUE)
                pass
            elif token in [ZCodeParser.FALSE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 257
                self.match(ZCodeParser.FALSE)
                pass
            elif token in [ZCodeParser.LBRACKET]:
                self.enterOuterAlt(localctx, 5)
                self.state = 258
                self.array_literal()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACKET(self):
            return self.getToken(ZCodeParser.LBRACKET, 0)

        def list_expression(self):
            return self.getTypedRuleContext(ZCodeParser.List_expressionContext,0)


        def RBRACKET(self):
            return self.getToken(ZCodeParser.RBRACKET, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_array_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_literal" ):
                return visitor.visitArray_literal(self)
            else:
                return visitor.visitChildren(self)




    def array_literal(self):

        localctx = ZCodeParser.Array_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_array_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 261
            self.match(ZCodeParser.LBRACKET)
            self.state = 262
            self.list_expression()
            self.state = 263
            self.match(ZCodeParser.RBRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def LPAREN(self):
            return self.getToken(ZCodeParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(ZCodeParser.RPAREN, 0)

        def list_expression(self):
            return self.getTypedRuleContext(ZCodeParser.List_expressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_func_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call" ):
                return visitor.visitFunc_call(self)
            else:
                return visitor.visitChildren(self)




    def func_call(self):

        localctx = ZCodeParser.Func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_func_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            self.match(ZCodeParser.ID)
            self.state = 266
            self.match(ZCodeParser.LPAREN)
            self.state = 268
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.TRUE) | (1 << ZCodeParser.FALSE) | (1 << ZCodeParser.NOT) | (1 << ZCodeParser.ADD) | (1 << ZCodeParser.SUB) | (1 << ZCodeParser.LBRACKET) | (1 << ZCodeParser.LPAREN) | (1 << ZCodeParser.ID) | (1 << ZCodeParser.NUMBER_LIT) | (1 << ZCodeParser.STRING_LIT))) != 0):
                self.state = 267
                self.list_expression()


            self.state = 270
            self.match(ZCodeParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IgnoreContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_ignore

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIgnore" ):
                return visitor.visitIgnore(self)
            else:
                return visitor.visitChildren(self)




    def ignore(self):

        localctx = ZCodeParser.IgnoreContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_ignore)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 273 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 272
                self.match(ZCodeParser.NEWLINE)
                self.state = 275 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ZCodeParser.NEWLINE):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Declaration_statementContext,0)


        def assignment_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Assignment_statementContext,0)


        def if_statement(self):
            return self.getTypedRuleContext(ZCodeParser.If_statementContext,0)


        def for_statement(self):
            return self.getTypedRuleContext(ZCodeParser.For_statementContext,0)


        def break_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Break_statementContext,0)


        def continue_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Continue_statementContext,0)


        def return_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Return_statementContext,0)


        def call_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Call_statementContext,0)


        def block_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Block_statementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = ZCodeParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_statement)
        try:
            self.state = 286
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 277
                self.declaration_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 278
                self.assignment_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 279
                self.if_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 280
                self.for_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 281
                self.break_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 282
                self.continue_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 283
                self.return_statement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 284
                self.call_statement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 285
                self.block_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declaration_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def implicit_var(self):
            return self.getTypedRuleContext(ZCodeParser.Implicit_varContext,0)


        def keyword_var(self):
            return self.getTypedRuleContext(ZCodeParser.Keyword_varContext,0)


        def implicit_dynamic(self):
            return self.getTypedRuleContext(ZCodeParser.Implicit_dynamicContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_declaration_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration_statement" ):
                return visitor.visitDeclaration_statement(self)
            else:
                return visitor.visitChildren(self)




    def declaration_statement(self):

        localctx = ZCodeParser.Declaration_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_declaration_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 291
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.VAR]:
                self.state = 288
                self.implicit_var()
                pass
            elif token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING]:
                self.state = 289
                self.keyword_var()
                pass
            elif token in [ZCodeParser.DYNAMIC]:
                self.state = 290
                self.implicit_dynamic()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 293
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(ZCodeParser.LhsContext,0)


        def ASSIGNINIT(self):
            return self.getToken(ZCodeParser.ASSIGNINIT, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_assignment_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_statement" ):
                return visitor.visitAssignment_statement(self)
            else:
                return visitor.visitChildren(self)




    def assignment_statement(self):

        localctx = ZCodeParser.Assignment_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_assignment_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 295
            self.lhs()
            self.state = 296
            self.match(ZCodeParser.ASSIGNINIT)
            self.state = 297
            self.expression()
            self.state = 298
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def LBRACKET(self):
            return self.getToken(ZCodeParser.LBRACKET, 0)

        def list_expression(self):
            return self.getTypedRuleContext(ZCodeParser.List_expressionContext,0)


        def RBRACKET(self):
            return self.getToken(ZCodeParser.RBRACKET, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = ZCodeParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_lhs)
        try:
            self.state = 306
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 300
                self.match(ZCodeParser.ID)
                self.state = 301
                self.match(ZCodeParser.LBRACKET)
                self.state = 302
                self.list_expression()
                self.state = 303
                self.match(ZCodeParser.RBRACKET)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 305
                self.match(ZCodeParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(ZCodeParser.IF, 0)

        def LPAREN(self):
            return self.getToken(ZCodeParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(ZCodeParser.RPAREN, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.StatementContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.StatementContext,i)


        def ignore(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.IgnoreContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.IgnoreContext,i)


        def elif_list(self):
            return self.getTypedRuleContext(ZCodeParser.Elif_listContext,0)


        def ELSE(self):
            return self.getToken(ZCodeParser.ELSE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_if_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = ZCodeParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_if_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 308
            self.match(ZCodeParser.IF)
            self.state = 309
            self.match(ZCodeParser.LPAREN)
            self.state = 310
            self.expression()
            self.state = 311
            self.match(ZCodeParser.RPAREN)
            self.state = 313
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.NEWLINE:
                self.state = 312
                self.ignore()


            self.state = 315
            self.statement()
            self.state = 317
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.state = 316
                self.elif_list()


            self.state = 324
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.state = 319
                self.match(ZCodeParser.ELSE)
                self.state = 321
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.NEWLINE:
                    self.state = 320
                    self.ignore()


                self.state = 323
                self.statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elif_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elif_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Elif_stmtContext,0)


        def elif_list(self):
            return self.getTypedRuleContext(ZCodeParser.Elif_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elif_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElif_list" ):
                return visitor.visitElif_list(self)
            else:
                return visitor.visitChildren(self)




    def elif_list(self):

        localctx = ZCodeParser.Elif_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_elif_list)
        try:
            self.state = 330
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 326
                self.elif_stmt()
                self.state = 327
                self.elif_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 329
                self.elif_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elif_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELIF(self):
            return self.getToken(ZCodeParser.ELIF, 0)

        def LPAREN(self):
            return self.getToken(ZCodeParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(ZCodeParser.RPAREN, 0)

        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elif_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElif_stmt" ):
                return visitor.visitElif_stmt(self)
            else:
                return visitor.visitChildren(self)




    def elif_stmt(self):

        localctx = ZCodeParser.Elif_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_elif_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 332
            self.match(ZCodeParser.ELIF)
            self.state = 333
            self.match(ZCodeParser.LPAREN)
            self.state = 334
            self.expression()
            self.state = 335
            self.match(ZCodeParser.RPAREN)
            self.state = 337
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.NEWLINE:
                self.state = 336
                self.ignore()


            self.state = 339
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(ZCodeParser.FOR, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def UNTIL(self):
            return self.getToken(ZCodeParser.UNTIL, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExpressionContext,i)


        def BY(self):
            return self.getToken(ZCodeParser.BY, 0)

        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_for_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_statement" ):
                return visitor.visitFor_statement(self)
            else:
                return visitor.visitChildren(self)




    def for_statement(self):

        localctx = ZCodeParser.For_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_for_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 341
            self.match(ZCodeParser.FOR)
            self.state = 342
            self.match(ZCodeParser.ID)
            self.state = 343
            self.match(ZCodeParser.UNTIL)
            self.state = 344
            self.expression()
            self.state = 345
            self.match(ZCodeParser.BY)
            self.state = 346
            self.expression()
            self.state = 348
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.NEWLINE:
                self.state = 347
                self.ignore()


            self.state = 350
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(ZCodeParser.BREAK, 0)

        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_break_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_statement" ):
                return visitor.visitBreak_statement(self)
            else:
                return visitor.visitChildren(self)




    def break_statement(self):

        localctx = ZCodeParser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 352
            self.match(ZCodeParser.BREAK)
            self.state = 353
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(ZCodeParser.CONTINUE, 0)

        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_continue_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_statement" ):
                return visitor.visitContinue_statement(self)
            else:
                return visitor.visitChildren(self)




    def continue_statement(self):

        localctx = ZCodeParser.Continue_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_continue_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 355
            self.match(ZCodeParser.CONTINUE)
            self.state = 356
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(ZCodeParser.RETURN, 0)

        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_return_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_statement" ):
                return visitor.visitReturn_statement(self)
            else:
                return visitor.visitChildren(self)




    def return_statement(self):

        localctx = ZCodeParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_return_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 358
            self.match(ZCodeParser.RETURN)
            self.state = 360
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.TRUE) | (1 << ZCodeParser.FALSE) | (1 << ZCodeParser.NOT) | (1 << ZCodeParser.ADD) | (1 << ZCodeParser.SUB) | (1 << ZCodeParser.LBRACKET) | (1 << ZCodeParser.LPAREN) | (1 << ZCodeParser.ID) | (1 << ZCodeParser.NUMBER_LIT) | (1 << ZCodeParser.STRING_LIT))) != 0):
                self.state = 359
                self.expression()


            self.state = 362
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def func_call(self):
            return self.getTypedRuleContext(ZCodeParser.Func_callContext,0)


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_call_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_statement" ):
                return visitor.visitCall_statement(self)
            else:
                return visitor.visitChildren(self)




    def call_statement(self):

        localctx = ZCodeParser.Call_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_call_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 364
            self.func_call()
            self.state = 365
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGIN(self):
            return self.getToken(ZCodeParser.BEGIN, 0)

        def ignore(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.IgnoreContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.IgnoreContext,i)


        def stmt_list(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_listContext,0)


        def END(self):
            return self.getToken(ZCodeParser.END, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_block_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_statement" ):
                return visitor.visitBlock_statement(self)
            else:
                return visitor.visitChildren(self)




    def block_statement(self):

        localctx = ZCodeParser.Block_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_block_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 367
            self.match(ZCodeParser.BEGIN)
            self.state = 368
            self.ignore()
            self.state = 369
            self.stmt_list()
            self.state = 370
            self.match(ZCodeParser.END)
            self.state = 371
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def stmt_list(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_list" ):
                return visitor.visitStmt_list(self)
            else:
                return visitor.visitChildren(self)




    def stmt_list(self):

        localctx = ZCodeParser.Stmt_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_stmt_list)
        try:
            self.state = 377
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.RETURN, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FOR, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.IF, ZCodeParser.BEGIN, ZCodeParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 373
                self.statement()
                self.state = 374
                self.stmt_list()
                pass
            elif token in [ZCodeParser.END]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[15] = self.expr2_sempred
        self._predicates[16] = self.expr3_sempred
        self._predicates[17] = self.expr4_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr4_sempred(self, localctx:Expr4Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




