import React, { useState, useEffect } from "react";
import { Container, Row, Col, Card, CardHeader, CardBody } from "shards-react";
import axios from 'axios';

import PageTitle from "../components/common/PageTitle";

const Tables = () => {

  const [riderInfo, getRiderInfo] = useState([
    '',
    '',
    '',
    '',
    ''
  ])

  const apiEndPoint = "https://64mg85mq2c.execute-api.us-east-1.amazonaws.com/hella/rank";
  const getRiders = async () => {
    await axios.get(apiEndPoint).then((res) => {
        const data = res.data;
        console.log("data", data)
        getRiderInfo(data['body'])
    });
  };

  useEffect(() => {
    getRiders()
    console.log("asdasd", riderInfo[0])
  }, []);

  const bestRiderList = riderInfo.slice(0,5).map((rider, idx) => (
    <tr>
      <td>{idx+1}</td>
      <td>{rider[0]}</td>
      <td>{rider[1]}세</td>
      <td>{parseFloat(rider[2]).toFixed(2)}km</td>
      <td>{parseFloat(rider[3]).toFixed(1)}회</td>
      <td>{rider[4]}</td>
    </tr>
  ))

  const worstRiderList = riderInfo.slice(5,10).map((rider, idx) => (
    <tr>
      <td>{idx+1}</td>
      <td>{rider[0]}</td>
      <td>{rider[1]}세</td>
      <td>{parseFloat(rider[2]).toFixed(2)}km</td>
      <td>{parseFloat(rider[3]).toFixed(1)}회</td>
      <td>{rider[4]}</td>
    </tr>
  ))

  return (
    <Container fluid className="main-content-container px-4">
      {/* Page Header */}
      <Row noGutters className="page-header py-4">
        <PageTitle sm="4" title="라이더 평가 정보" subtitle="HellaRiders" className="text-sm-left" />
      </Row>

      {/* Default Light Table */}
      <Row>
        <Col>
          <Card small className="mb-4">
            <CardHeader className="border-bottom">
              <h6 className="m-0">Best Rider</h6>
            </CardHeader>
            <CardBody className="p-0 pb-3">
              <table className="table mb-0">
                <thead className="bg-light">
                  <tr>
                    <th scope="col" className="border-0">
                    </th>
                    <th scope="col" className="border-0">
                      Rider ID
                    </th>
                    <th scope="col" className="border-0">
                      나이
                    </th>
                    <th scope="col" className="border-0">
                      주행거리
                    </th>
                    <th scope="col" className="border-0">
                      위험 알람 횟수
                    </th>
                    <th scope="col" className="border-0">
                      등급
                    </th>
                  </tr>
                </thead>
                <tbody>
                  {bestRiderList}                
                </tbody>
              </table>
            </CardBody>
          </Card>
        </Col>
      </Row>

      {/* Default Dark Table */}
      <Row>
        <Col>
          <Card small className="mb-4 overflow-hidden">
            <CardHeader className="bg-dark">
              <h6 className="m-0 text-white">Worst Rider</h6>
            </CardHeader>
            <CardBody className="bg-dark p-0 pb-3">
              <table className="table table-dark mb-0">
                <thead className="thead-dark">
                  <tr>
                    <th scope="col" className="border-0">
                    </th>
                    <th scope="col" className="border-0">
                      Rider ID
                    </th>
                    <th scope="col" className="border-0">
                      나이
                    </th>
                    <th scope="col" className="border-0">
                      주행거리
                    </th>
                    <th scope="col" className="border-0">
                      위험 알람 횟수
                    </th>
                    <th scope="col" className="border-0">
                      등급
                    </th>
                  </tr>
                </thead>
                <tbody>
                  {worstRiderList}
                </tbody>
              </table>
            </CardBody>
          </Card>
        </Col>
      </Row>
    </Container>
  )
};

export default Tables;
