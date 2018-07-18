FROM python

WORKDIR /root

ADD setup.py setup.py
ADD helpdful helpdful

RUN pip install .

# there's a stray xrange in the svglib even though it shouldn't be present, so let's fix it!
RUN sed -i.bak -e 's/xrange/range/g' /usr/local/lib/python3.7/site-packages/svglib/svglib.py

CMD python -m helpdful
