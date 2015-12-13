from bucket_filter import get_bucket


START = "("
END = ")"
AND = "&"
OR = "||"

# a & (b || c) || d & (e & F)
# t1 = e & f
# t2 = b || c
# t3 = a & t2 || d & t1


def parse(expression):
    # if expression[0] == START:
    #     expression = expression[1]
    # if expression[-1] == END:
    #     expression = expression[0:-1]
    if expression[0] == START and expression[-1] == END:
        expression = expression[1:-1]
    strt_index = expression.rfind(START)

    expressions = {}
    i = 0
    while(strt_index != -1):
        i += 1
        end_index = expression.find(END, strt_index)
        eval__format = "{}".format(i)
        expressions[eval__format] = expression[strt_index: end_index + 1]
        expression = expression.replace(expressions[eval__format], eval__format)
        strt_index = expression.rfind(START, 0 , strt_index)

    expressions["FINAL"] = expression
    return (expressions, i)


def evaluate(current, evaluated):
    if current[0] == START:
        current = current[1]
    if current[-1] == END:
        current = current[0:-1]
    operator = AND if AND in current else OR
    l, r = [i.strip() for i in current.split(operator)]
    if l in evaluated:
        bucket_l = evaluated[l]
    else:
        bucket_l = get_bucket(l)
    if r in evaluated:
        bucket_r = get_bucket(r)
    else:
        bucket_r = get_bucket(r)
    if bucket_r and bucket_l:
        if operator == AND:
            pass
        else:
            pass

evaluate("a & b" , None, None)



