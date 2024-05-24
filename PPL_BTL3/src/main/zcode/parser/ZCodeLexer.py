# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


  #2153594
from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\64")
        buf.write("\u0182\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3")
        buf.write("\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3")
        buf.write("\r\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\26")
        buf.write("\3\26\3\26\3\26\3\27\3\27\3\27\3\30\3\30\3\31\3\31\3\32")
        buf.write("\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\36\3\37")
        buf.write("\3\37\3\37\3 \3 \3!\3!\3!\3\"\3\"\3#\3#\3#\3$\3$\3$\3")
        buf.write("%\3%\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\7+\u0119")
        buf.write("\n+\f+\16+\u011c\13+\3,\3,\5,\u0120\n,\3,\5,\u0123\n,")
        buf.write("\3-\6-\u0126\n-\r-\16-\u0127\3.\3.\7.\u012c\n.\f.\16.")
        buf.write("\u012f\13.\3/\3/\5/\u0133\n/\3/\6/\u0136\n/\r/\16/\u0137")
        buf.write("\3\60\3\60\3\61\3\61\7\61\u013e\n\61\f\61\16\61\u0141")
        buf.write("\13\61\3\61\3\61\3\61\3\62\3\62\3\63\3\63\3\63\3\63\7")
        buf.write("\63\u014c\n\63\f\63\16\63\u014f\13\63\3\63\3\63\3\64\6")
        buf.write("\64\u0154\n\64\r\64\16\64\u0155\3\64\3\64\3\65\3\65\7")
        buf.write("\65\u015c\n\65\f\65\16\65\u015f\13\65\3\65\3\65\3\65\5")
        buf.write("\65\u0164\n\65\3\65\3\65\3\66\3\66\7\66\u016a\n\66\f\66")
        buf.write("\16\66\u016d\13\66\3\66\3\66\3\66\3\67\3\67\3\67\5\67")
        buf.write("\u0175\n\67\38\38\38\38\58\u017b\n8\39\39\39\3:\3:\3:")
        buf.write("\2\2;\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27")
        buf.write("\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30")
        buf.write("/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'")
        buf.write("M(O)Q*S+U,W-Y\2[\2]\2_\2a.c/e\60g\61i\62k\63m\2o\2q\2")
        buf.write("s\64\3\2\20\5\2C\\aac|\6\2\62;C\\aac|\4\2GGgg\4\2--//")
        buf.write("\3\2\62;\3\2\f\f\4\2\f\f\16\17\5\2\13\13\17\17\"\"\3\3")
        buf.write("\f\f\t\2))^^ddhhppttvv\3\2\16\17\6\2\f\f\16\17$$^^\3\2")
        buf.write("))\3\2$$\2\u018a\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2")
        buf.write("\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2")
        buf.write("\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2")
        buf.write("\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2")
        buf.write("\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2")
        buf.write("\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3")
        buf.write("\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q")
        buf.write("\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2a\3\2\2\2\2")
        buf.write("c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2")
        buf.write("\2s\3\2\2\2\3u\3\2\2\2\5z\3\2\2\2\7\u0080\3\2\2\2\t\u0087")
        buf.write("\3\2\2\2\13\u008c\3\2\2\2\r\u0093\3\2\2\2\17\u009a\3\2")
        buf.write("\2\2\21\u009e\3\2\2\2\23\u00a6\3\2\2\2\25\u00ab\3\2\2")
        buf.write("\2\27\u00af\3\2\2\2\31\u00b5\3\2\2\2\33\u00b8\3\2\2\2")
        buf.write("\35\u00be\3\2\2\2\37\u00c7\3\2\2\2!\u00ca\3\2\2\2#\u00cf")
        buf.write("\3\2\2\2%\u00d4\3\2\2\2\'\u00da\3\2\2\2)\u00de\3\2\2\2")
        buf.write("+\u00e2\3\2\2\2-\u00e6\3\2\2\2/\u00e9\3\2\2\2\61\u00eb")
        buf.write("\3\2\2\2\63\u00ed\3\2\2\2\65\u00ef\3\2\2\2\67\u00f1\3")
        buf.write("\2\2\29\u00f3\3\2\2\2;\u00f5\3\2\2\2=\u00f8\3\2\2\2?\u00fb")
        buf.write("\3\2\2\2A\u00fd\3\2\2\2C\u0100\3\2\2\2E\u0102\3\2\2\2")
        buf.write("G\u0105\3\2\2\2I\u0108\3\2\2\2K\u010c\3\2\2\2M\u010e\3")
        buf.write("\2\2\2O\u0110\3\2\2\2Q\u0112\3\2\2\2S\u0114\3\2\2\2U\u0116")
        buf.write("\3\2\2\2W\u011d\3\2\2\2Y\u0125\3\2\2\2[\u0129\3\2\2\2")
        buf.write("]\u0130\3\2\2\2_\u0139\3\2\2\2a\u013b\3\2\2\2c\u0145\3")
        buf.write("\2\2\2e\u0147\3\2\2\2g\u0153\3\2\2\2i\u0159\3\2\2\2k\u0167")
        buf.write("\3\2\2\2m\u0174\3\2\2\2o\u017a\3\2\2\2q\u017c\3\2\2\2")
        buf.write("s\u017f\3\2\2\2uv\7v\2\2vw\7t\2\2wx\7w\2\2xy\7g\2\2y\4")
        buf.write("\3\2\2\2z{\7h\2\2{|\7c\2\2|}\7n\2\2}~\7u\2\2~\177\7g\2")
        buf.write("\2\177\6\3\2\2\2\u0080\u0081\7p\2\2\u0081\u0082\7w\2\2")
        buf.write("\u0082\u0083\7o\2\2\u0083\u0084\7d\2\2\u0084\u0085\7g")
        buf.write("\2\2\u0085\u0086\7t\2\2\u0086\b\3\2\2\2\u0087\u0088\7")
        buf.write("d\2\2\u0088\u0089\7q\2\2\u0089\u008a\7q\2\2\u008a\u008b")
        buf.write("\7n\2\2\u008b\n\3\2\2\2\u008c\u008d\7u\2\2\u008d\u008e")
        buf.write("\7v\2\2\u008e\u008f\7t\2\2\u008f\u0090\7k\2\2\u0090\u0091")
        buf.write("\7p\2\2\u0091\u0092\7i\2\2\u0092\f\3\2\2\2\u0093\u0094")
        buf.write("\7t\2\2\u0094\u0095\7g\2\2\u0095\u0096\7v\2\2\u0096\u0097")
        buf.write("\7w\2\2\u0097\u0098\7t\2\2\u0098\u0099\7p\2\2\u0099\16")
        buf.write("\3\2\2\2\u009a\u009b\7x\2\2\u009b\u009c\7c\2\2\u009c\u009d")
        buf.write("\7t\2\2\u009d\20\3\2\2\2\u009e\u009f\7f\2\2\u009f\u00a0")
        buf.write("\7{\2\2\u00a0\u00a1\7p\2\2\u00a1\u00a2\7c\2\2\u00a2\u00a3")
        buf.write("\7o\2\2\u00a3\u00a4\7k\2\2\u00a4\u00a5\7e\2\2\u00a5\22")
        buf.write("\3\2\2\2\u00a6\u00a7\7h\2\2\u00a7\u00a8\7w\2\2\u00a8\u00a9")
        buf.write("\7p\2\2\u00a9\u00aa\7e\2\2\u00aa\24\3\2\2\2\u00ab\u00ac")
        buf.write("\7h\2\2\u00ac\u00ad\7q\2\2\u00ad\u00ae\7t\2\2\u00ae\26")
        buf.write("\3\2\2\2\u00af\u00b0\7w\2\2\u00b0\u00b1\7p\2\2\u00b1\u00b2")
        buf.write("\7v\2\2\u00b2\u00b3\7k\2\2\u00b3\u00b4\7n\2\2\u00b4\30")
        buf.write("\3\2\2\2\u00b5\u00b6\7d\2\2\u00b6\u00b7\7{\2\2\u00b7\32")
        buf.write("\3\2\2\2\u00b8\u00b9\7d\2\2\u00b9\u00ba\7t\2\2\u00ba\u00bb")
        buf.write("\7g\2\2\u00bb\u00bc\7c\2\2\u00bc\u00bd\7m\2\2\u00bd\34")
        buf.write("\3\2\2\2\u00be\u00bf\7e\2\2\u00bf\u00c0\7q\2\2\u00c0\u00c1")
        buf.write("\7p\2\2\u00c1\u00c2\7v\2\2\u00c2\u00c3\7k\2\2\u00c3\u00c4")
        buf.write("\7p\2\2\u00c4\u00c5\7w\2\2\u00c5\u00c6\7g\2\2\u00c6\36")
        buf.write("\3\2\2\2\u00c7\u00c8\7k\2\2\u00c8\u00c9\7h\2\2\u00c9 ")
        buf.write("\3\2\2\2\u00ca\u00cb\7g\2\2\u00cb\u00cc\7n\2\2\u00cc\u00cd")
        buf.write("\7u\2\2\u00cd\u00ce\7g\2\2\u00ce\"\3\2\2\2\u00cf\u00d0")
        buf.write("\7g\2\2\u00d0\u00d1\7n\2\2\u00d1\u00d2\7k\2\2\u00d2\u00d3")
        buf.write("\7h\2\2\u00d3$\3\2\2\2\u00d4\u00d5\7d\2\2\u00d5\u00d6")
        buf.write("\7g\2\2\u00d6\u00d7\7i\2\2\u00d7\u00d8\7k\2\2\u00d8\u00d9")
        buf.write("\7p\2\2\u00d9&\3\2\2\2\u00da\u00db\7g\2\2\u00db\u00dc")
        buf.write("\7p\2\2\u00dc\u00dd\7f\2\2\u00dd(\3\2\2\2\u00de\u00df")
        buf.write("\7p\2\2\u00df\u00e0\7q\2\2\u00e0\u00e1\7v\2\2\u00e1*\3")
        buf.write("\2\2\2\u00e2\u00e3\7c\2\2\u00e3\u00e4\7p\2\2\u00e4\u00e5")
        buf.write("\7f\2\2\u00e5,\3\2\2\2\u00e6\u00e7\7q\2\2\u00e7\u00e8")
        buf.write("\7t\2\2\u00e8.\3\2\2\2\u00e9\u00ea\7-\2\2\u00ea\60\3\2")
        buf.write("\2\2\u00eb\u00ec\7/\2\2\u00ec\62\3\2\2\2\u00ed\u00ee\7")
        buf.write(",\2\2\u00ee\64\3\2\2\2\u00ef\u00f0\7\61\2\2\u00f0\66\3")
        buf.write("\2\2\2\u00f1\u00f2\7\'\2\2\u00f28\3\2\2\2\u00f3\u00f4")
        buf.write("\7?\2\2\u00f4:\3\2\2\2\u00f5\u00f6\7#\2\2\u00f6\u00f7")
        buf.write("\7?\2\2\u00f7<\3\2\2\2\u00f8\u00f9\7>\2\2\u00f9\u00fa")
        buf.write("\7/\2\2\u00fa>\3\2\2\2\u00fb\u00fc\7>\2\2\u00fc@\3\2\2")
        buf.write("\2\u00fd\u00fe\7>\2\2\u00fe\u00ff\7?\2\2\u00ffB\3\2\2")
        buf.write("\2\u0100\u0101\7@\2\2\u0101D\3\2\2\2\u0102\u0103\7@\2")
        buf.write("\2\u0103\u0104\7?\2\2\u0104F\3\2\2\2\u0105\u0106\7?\2")
        buf.write("\2\u0106\u0107\7?\2\2\u0107H\3\2\2\2\u0108\u0109\7\60")
        buf.write("\2\2\u0109\u010a\7\60\2\2\u010a\u010b\7\60\2\2\u010bJ")
        buf.write("\3\2\2\2\u010c\u010d\7]\2\2\u010dL\3\2\2\2\u010e\u010f")
        buf.write("\7_\2\2\u010fN\3\2\2\2\u0110\u0111\7*\2\2\u0111P\3\2\2")
        buf.write("\2\u0112\u0113\7+\2\2\u0113R\3\2\2\2\u0114\u0115\7.\2")
        buf.write("\2\u0115T\3\2\2\2\u0116\u011a\t\2\2\2\u0117\u0119\t\3")
        buf.write("\2\2\u0118\u0117\3\2\2\2\u0119\u011c\3\2\2\2\u011a\u0118")
        buf.write("\3\2\2\2\u011a\u011b\3\2\2\2\u011bV\3\2\2\2\u011c\u011a")
        buf.write("\3\2\2\2\u011d\u011f\5Y-\2\u011e\u0120\5[.\2\u011f\u011e")
        buf.write("\3\2\2\2\u011f\u0120\3\2\2\2\u0120\u0122\3\2\2\2\u0121")
        buf.write("\u0123\5]/\2\u0122\u0121\3\2\2\2\u0122\u0123\3\2\2\2\u0123")
        buf.write("X\3\2\2\2\u0124\u0126\5_\60\2\u0125\u0124\3\2\2\2\u0126")
        buf.write("\u0127\3\2\2\2\u0127\u0125\3\2\2\2\u0127\u0128\3\2\2\2")
        buf.write("\u0128Z\3\2\2\2\u0129\u012d\7\60\2\2\u012a\u012c\5_\60")
        buf.write("\2\u012b\u012a\3\2\2\2\u012c\u012f\3\2\2\2\u012d\u012b")
        buf.write("\3\2\2\2\u012d\u012e\3\2\2\2\u012e\\\3\2\2\2\u012f\u012d")
        buf.write("\3\2\2\2\u0130\u0132\t\4\2\2\u0131\u0133\t\5\2\2\u0132")
        buf.write("\u0131\3\2\2\2\u0132\u0133\3\2\2\2\u0133\u0135\3\2\2\2")
        buf.write("\u0134\u0136\5_\60\2\u0135\u0134\3\2\2\2\u0136\u0137\3")
        buf.write("\2\2\2\u0137\u0135\3\2\2\2\u0137\u0138\3\2\2\2\u0138^")
        buf.write("\3\2\2\2\u0139\u013a\t\6\2\2\u013a`\3\2\2\2\u013b\u013f")
        buf.write("\7$\2\2\u013c\u013e\5o8\2\u013d\u013c\3\2\2\2\u013e\u0141")
        buf.write("\3\2\2\2\u013f\u013d\3\2\2\2\u013f\u0140\3\2\2\2\u0140")
        buf.write("\u0142\3\2\2\2\u0141\u013f\3\2\2\2\u0142\u0143\7$\2\2")
        buf.write("\u0143\u0144\b\61\2\2\u0144b\3\2\2\2\u0145\u0146\t\7\2")
        buf.write("\2\u0146d\3\2\2\2\u0147\u0148\7%\2\2\u0148\u0149\7%\2")
        buf.write("\2\u0149\u014d\3\2\2\2\u014a\u014c\n\b\2\2\u014b\u014a")
        buf.write("\3\2\2\2\u014c\u014f\3\2\2\2\u014d\u014b\3\2\2\2\u014d")
        buf.write("\u014e\3\2\2\2\u014e\u0150\3\2\2\2\u014f\u014d\3\2\2\2")
        buf.write("\u0150\u0151\b\63\3\2\u0151f\3\2\2\2\u0152\u0154\t\t\2")
        buf.write("\2\u0153\u0152\3\2\2\2\u0154\u0155\3\2\2\2\u0155\u0153")
        buf.write("\3\2\2\2\u0155\u0156\3\2\2\2\u0156\u0157\3\2\2\2\u0157")
        buf.write("\u0158\b\64\3\2\u0158h\3\2\2\2\u0159\u015d\7$\2\2\u015a")
        buf.write("\u015c\5o8\2\u015b\u015a\3\2\2\2\u015c\u015f\3\2\2\2\u015d")
        buf.write("\u015b\3\2\2\2\u015d\u015e\3\2\2\2\u015e\u0163\3\2\2\2")
        buf.write("\u015f\u015d\3\2\2\2\u0160\u0161\7\17\2\2\u0161\u0164")
        buf.write("\7\f\2\2\u0162\u0164\t\n\2\2\u0163\u0160\3\2\2\2\u0163")
        buf.write("\u0162\3\2\2\2\u0164\u0165\3\2\2\2\u0165\u0166\b\65\4")
        buf.write("\2\u0166j\3\2\2\2\u0167\u016b\7$\2\2\u0168\u016a\5o8\2")
        buf.write("\u0169\u0168\3\2\2\2\u016a\u016d\3\2\2\2\u016b\u0169\3")
        buf.write("\2\2\2\u016b\u016c\3\2\2\2\u016c\u016e\3\2\2\2\u016d\u016b")
        buf.write("\3\2\2\2\u016e\u016f\5m\67\2\u016f\u0170\b\66\5\2\u0170")
        buf.write("l\3\2\2\2\u0171\u0172\7^\2\2\u0172\u0175\n\13\2\2\u0173")
        buf.write("\u0175\t\f\2\2\u0174\u0171\3\2\2\2\u0174\u0173\3\2\2\2")
        buf.write("\u0175n\3\2\2\2\u0176\u017b\n\r\2\2\u0177\u017b\5q9\2")
        buf.write("\u0178\u0179\t\16\2\2\u0179\u017b\t\17\2\2\u017a\u0176")
        buf.write("\3\2\2\2\u017a\u0177\3\2\2\2\u017a\u0178\3\2\2\2\u017b")
        buf.write("p\3\2\2\2\u017c\u017d\7^\2\2\u017d\u017e\t\13\2\2\u017e")
        buf.write("r\3\2\2\2\u017f\u0180\13\2\2\2\u0180\u0181\b:\6\2\u0181")
        buf.write("t\3\2\2\2\22\2\u011a\u011f\u0122\u0127\u012d\u0132\u0137")
        buf.write("\u013f\u014d\u0155\u015d\u0163\u016b\u0174\u017a\7\3\61")
        buf.write("\2\b\2\2\3\65\3\3\66\4\3:\5")
        return buf.getvalue()


class ZCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    TRUE = 1
    FALSE = 2
    NUMBER = 3
    BOOL = 4
    STRING = 5
    RETURN = 6
    VAR = 7
    DYNAMIC = 8
    FUNC = 9
    FOR = 10
    UNTIL = 11
    BY = 12
    BREAK = 13
    CONTINUE = 14
    IF = 15
    ELSE = 16
    ELIF = 17
    BEGIN = 18
    END = 19
    NOT = 20
    AND = 21
    OR = 22
    ADD = 23
    SUB = 24
    MUL = 25
    DIV = 26
    MOD = 27
    EQUAL = 28
    NOT_EQUAL = 29
    ASSIGNINIT = 30
    LESS_THAN = 31
    LESS_THAN_EQUAL = 32
    GREATER_THAN = 33
    GREATER_THAN_EQUAL = 34
    STRING_EQUAL = 35
    STRING_CONCAT = 36
    LBRACKET = 37
    RBRACKET = 38
    LPAREN = 39
    RPAREN = 40
    COMMA = 41
    ID = 42
    NUMBER_LIT = 43
    STRING_LIT = 44
    NEWLINE = 45
    COMMENTS = 46
    WS = 47
    UNCLOSE_STRING = 48
    ILLEGAL_ESCAPE = 49
    ERROR_CHAR = 50

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'true'", "'false'", "'number'", "'bool'", "'string'", "'return'", 
            "'var'", "'dynamic'", "'func'", "'for'", "'until'", "'by'", 
            "'break'", "'continue'", "'if'", "'else'", "'elif'", "'begin'", 
            "'end'", "'not'", "'and'", "'or'", "'+'", "'-'", "'*'", "'/'", 
            "'%'", "'='", "'!='", "'<-'", "'<'", "'<='", "'>'", "'>='", 
            "'=='", "'...'", "'['", "']'", "'('", "')'", "','" ]

    symbolicNames = [ "<INVALID>",
            "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", "RETURN", "VAR", 
            "DYNAMIC", "FUNC", "FOR", "UNTIL", "BY", "BREAK", "CONTINUE", 
            "IF", "ELSE", "ELIF", "BEGIN", "END", "NOT", "AND", "OR", "ADD", 
            "SUB", "MUL", "DIV", "MOD", "EQUAL", "NOT_EQUAL", "ASSIGNINIT", 
            "LESS_THAN", "LESS_THAN_EQUAL", "GREATER_THAN", "GREATER_THAN_EQUAL", 
            "STRING_EQUAL", "STRING_CONCAT", "LBRACKET", "RBRACKET", "LPAREN", 
            "RPAREN", "COMMA", "ID", "NUMBER_LIT", "STRING_LIT", "NEWLINE", 
            "COMMENTS", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", "RETURN", 
                  "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", "BY", "BREAK", 
                  "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", "END", "NOT", 
                  "AND", "OR", "ADD", "SUB", "MUL", "DIV", "MOD", "EQUAL", 
                  "NOT_EQUAL", "ASSIGNINIT", "LESS_THAN", "LESS_THAN_EQUAL", 
                  "GREATER_THAN", "GREATER_THAN_EQUAL", "STRING_EQUAL", 
                  "STRING_CONCAT", "LBRACKET", "RBRACKET", "LPAREN", "RPAREN", 
                  "COMMA", "ID", "NUMBER_LIT", "INTERGER_PART", "DECIMAL_PART", 
                  "EXPONENT_PART", "DIGIT", "STRING_LIT", "NEWLINE", "COMMENTS", 
                  "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ESC_ILLEGAL", 
                  "STR_CHAR", "ESC_SEQ", "ERROR_CHAR" ]

    grammarFileName = "ZCode.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[47] = self.STRING_LIT_action 
            actions[51] = self.UNCLOSE_STRING_action 
            actions[52] = self.ILLEGAL_ESCAPE_action 
            actions[56] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text[1:-1];
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

            	if(len(self.text) >= 2 and self.text[-1] == '\n' and self.text[-2] == '\r'):
            		raise UncloseString(self.text[1:-2])
            	elif (self.text[-1] == '\n'):
            		raise UncloseString(self.text[1:-1])
            	else:
            		raise UncloseString(self.text[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                raise IllegalEscape(self.text[1:])

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise ErrorToken(self.text)
     


